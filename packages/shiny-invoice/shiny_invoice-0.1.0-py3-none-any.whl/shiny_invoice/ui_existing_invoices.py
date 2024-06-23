"""This module contains the ui and server configurations for the existing invoices."""

import datetime
import glob
from pathlib import Path

import pandas as pd
from shiny import module, ui, render, reactive


@module.ui
def existing_invoices_ui():
    """Defines the shiny ui for existing invoices"""
    return ui.div(
        ui.card(
            ui.card_header("Filter"),
            ui.layout_columns(
                ui.tooltip(
                    ui.input_text("invoice_numbers", "Filter by invoices", placeholder="13,21,37"),
                    "Comma separated",
                ),
                ui.input_date_range(
                    id="daterange",
                    label="Filter by Date range",
                    start=f"{datetime.date.today().year}-01-01",
                ),
                ui.input_checkbox_group(
                    id="paid_status",
                    label="Paid Status",
                    choices={"paid": "Paid", "unpaid": "Unpaid"},
                    inline=True,
                ),
            ),
        ),
        ui.card(
            ui.layout_column_wrap(
                ui.card(
                    ui.card_header("List of filtered invoices"),
                    ui.output_data_frame("invoice_list"),
                ),
                ui.card(ui.card_header("Selected Invoice"), ui.output_ui("selected_invoice")),
            )
        ),
    )


@module.server
def existing_invoices_server(input, output, session, config):
    """Contains the Shiny Server for existing invoices"""

    @reactive.calc
    def get_filtered_invoices() -> pd.DataFrame | str:
        """Retrieve all invoices from the configured directories and parse them into a DataFrame.
        The input filters will then be applied to the dataframe such that only the desired results
        will be returned.
        """
        paid_records, unpaid_records = _get_invoice_records()
        df = pd.DataFrame.from_records(paid_records + unpaid_records)
        if len(df) == 0:
            return df
        duplicate_numbers = df[df.duplicated(["Invoice"], keep="last")]
        if len(duplicate_numbers) > 0:
            duplicate_ids = ", ".join(duplicate_numbers["Invoice"].to_list())
            ui.notification_show(
                f"Found duplicate invoice ids: {duplicate_ids}", type="warning", duration=2
            )
        df = _filter_invoices(df)
        return df

    def _get_invoice_records():
        root_dir = Path(config.get("paths").get("invoices_root_dir"))
        paid_dir = root_dir / config.get("paths").get("invoices_dir_paid")
        unpaid_dir = root_dir / config.get("paths").get("invoices_dir_unpaid")
        paid_invoices = glob.glob(f"{paid_dir}/**/*.html", recursive=True)
        unpaid_invoices = glob.glob(f"{unpaid_dir}/**/*.html", recursive=True)
        paid_records = _create_invoice_records(paid_invoices, status="paid")
        unpaid_records = _create_invoice_records(unpaid_invoices, status="unpaid")
        return paid_records, unpaid_records

    def _filter_invoices(df):
        if input.invoice_numbers():
            filtered_invoice_ids = input.invoice_numbers().split(",")
            df = df.loc[df["Invoice"].isin(filtered_invoice_ids)]
        if input.paid_status():
            df = df.loc[df["Status"].isin(input.paid_status())]
        start_date = input.daterange()[0]
        end_date = input.daterange()[1]
        df = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]
        df["Date"] = df["Date"].apply(lambda x: x.strftime("%d.%m.%Y"))
        return df

    def _create_invoice_records(file_paths, status):
        records = []
        for invoice_path in file_paths:
            parts = invoice_path.split("/")
            name_parts = parts[-1].split("-")
            date = datetime.date(
                year=int(name_parts[0]), month=int(name_parts[1]), day=int(name_parts[2])
            )
            invoice_number = name_parts[3]
            customer = name_parts[-1].replace(".html", "")
            root_dir = config.get("paths").get("invoices_root_dir")
            invoice_path = invoice_path.replace(root_dir, "")
            records.append(
                {
                    "Date": date,
                    "Invoice": invoice_number,
                    "Status": status,
                    "Customer": customer,
                    "Link": ui.a("Download", href=invoice_path, target="_blank"),
                }
            )
        return records

    @render.data_frame
    def invoice_list():
        """Render a list of filtered invoices"""
        df = get_filtered_invoices()
        return render.DataGrid(df, selection_mode="rows", width="100%")

    @render.ui
    def selected_invoice():
        """Render the currently selected invoice"""
        selection = invoice_list.cell_selection()["rows"]
        if len(selection) > 0:
            selection = selection[0]
            df = get_filtered_invoices().iloc[selection]["Link"]
            root_dir = Path(config.get("paths").get("invoices_root_dir"))
            with open(root_dir / df.attrs.get("href"), "r", encoding="utf8") as file:
                html = file.read()
            return ui.HTML(html)
        return selection

"""This module contains the ui and the server for creating a new invoice."""

import datetime
import io
from pathlib import Path
from string import Template

import pandas as pd
from shiny import module, ui, render, reactive


@module.ui
def new_invoice_ui(config):
    """Defines the shiny ui for new invoices"""
    invoice_defaults = config.get("invoice_defaults")

    return ui.layout_column_wrap(
        ui.card(
            ui.card_header("Invoice Details"),
            ui.input_text(id="invoice_number", label="Invoice Number", value="1", width="100%"),
            ui.input_date(id="created_at_date", label="Created At", width="100%"),
            ui.output_ui(id="due_date_ui", width="100%"),
            ui.input_text(
                id="introduction", label="Introduction", value="Dear Sir or Madam,", width="100%"
            ),
            ui.input_text_area(
                id="recipient_address",
                label="Recipient Address",
                value=invoice_defaults.get("recipient"),
                rows=3,
                width="100%",
            ),
            ui.tooltip(
                ui.input_text_area(
                    id="invoice_items",
                    label="Invoice Items",
                    value=invoice_defaults.get("items"),
                    rows=6,
                    width="100%",
                    spellcheck=True,
                ),
                "Should be in csv format. The last column will be used to calculate the"
                "total price. The values should be before taxes.",
            ),
            ui.download_button(id="download_button", label="Download Invoice", width="100%"),
        ),
        ui.card(
            ui.card_header("Rendered Invoice"), ui.output_ui(id="rendered_invoice_ui", width="100%")
        ),
    )


@module.server
def new_invoice_server(input, output, session, config):

    with open(Path(config.get("paths").get("html_template")), "r", encoding="utf8") as file:
        html_template = Template(file.read())

    @reactive.calc
    def parse_invoice_items() -> pd.DataFrame:
        return pd.read_csv(io.StringIO(input.invoice_items()), sep=",")

    @reactive.calc
    def convert_invoice_csv_to_html() -> str:
        return parse_invoice_items().to_html(index=False, border=0)

    @reactive.calc
    def calculate_totals():
        items = parse_invoice_items()
        last_column = items.columns[-1]
        items[last_column] = (
            items[last_column].str.replace(".", "").str.replace("€", "").astype(float)
        )
        return items[last_column].sum()

    @render.ui
    def due_date_ui():
        payment_terms_days = config.get("company").get("payment_terms_days")
        due_date = input.created_at_date() + datetime.timedelta(days=payment_terms_days)
        return ui.input_date("due_date", "Due date", value=str(due_date), width="100%")

    @reactive.calc
    def customer_name():
        return input.recipient_address().split("\n")[0]

    @render.download(
        filename=lambda: f"{input.created_at_date()}-{input.invoice_number()}-{customer_name()}.html",
    )
    def download_button():
        """Download the currently created invoice"""
        with io.BytesIO() as buf:
            buf.write(render_invoice().encode("utf8"))
            yield buf.getvalue()

    @reactive.calc
    def render_invoice():
        total_net = calculate_totals()
        company = config.get("company")
        tax = total_net * float(company.get("tax_rate"))
        total_gross = total_net + tax
        substitutions = {
            "name": company.get("name"),
            "primary_skills": " | ".join(company.get("skills")[:2]),
            "all_skills": "<br/>".join(company.get("skills")),
            "piped_address": " | ".join(company.get("address")),
            "linebreaked_address": "<br/>".join(company.get("address")),
            "primary_contact": "<br/>".join(company.get("contact")[:2]),
            "bank": company.get("bank").get("name"),
            "iban": company.get("bank").get("iban"),
            "bic": company.get("bank").get("bic"),
            "tax_number": company.get("bank").get("tax_number"),
            "tax_rate": f"{float(company.get('tax_rate')) * 100}%",
            "all_contact": "<br/>".join(company.get("contact")),
            "invoice_number": input.invoice_number(),
            "created_at_date": input.created_at_date().strftime("%d.%m.%Y"),
            "due_at_date": input.due_date().strftime("%d.%m.%Y"),
            "introduction": input.introduction(),
            "recipient_address": "</br>".join(input.recipient_address().split("\n")),
            "invoice_items": convert_invoice_csv_to_html(),
            "total_net": f"{total_net:n} €",
            "tax": f"{tax:n} €",
            "total_gross": f"{total_gross:n} €",
        }
        return html_template.substitute(substitutions)

    @render.ui
    def rendered_invoice_ui():
        """Render the currently configured invoice"""
        return ui.HTML(render_invoice())

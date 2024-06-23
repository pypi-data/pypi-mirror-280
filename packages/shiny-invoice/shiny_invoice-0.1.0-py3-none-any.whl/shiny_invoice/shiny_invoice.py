"""
Shiny Invoice is a simple tool to create invoices and view existing once.
This module acts as the entrypoint, containing the main navigational layout and server,
as well as the cli.
"""

from pathlib import Path

import click
from ruamel.yaml import YAML
from shiny import App, Inputs, Outputs, Session, ui

from shiny_invoice.ui_config import config_ui, config_server
from shiny_invoice.ui_existing_invoices import existing_invoices_ui, existing_invoices_server
from shiny_invoice.ui_new_invoice import new_invoice_ui, new_invoice_server

yaml = YAML(typ="rt", pure=True)


@click.group(name="shiny-invoice")
def cli():
    """Shiny Invoice CLI"""


@cli.command(short_help="Run Shiny Invoice")
@click.option(
    "--config",
    type=click.Path(exists=True),
    required=True,
    help="Path to the configuration yaml file.",
)
@click.option(
    "--host", type=str, default="0.0.0.0", help="Host used for the server, defaults to '0.0.0.0'."
)
@click.option(
    "--port", type=int, default=8000, help="Port used for the server, defaults to '8000'."
)
def run(config: Path, host: str, port: int):
    """Run shiny invoice"""
    with open(config, "r", encoding="utf8") as file:
        config_str = file.read()
    config = yaml.load(config_str)

    # pylint: disable=too-many-function-args
    app_ui = ui.page_navbar(
        ui.nav_panel("Existing Invoices", existing_invoices_ui("existing_invoices")),
        ui.nav_panel("Create Invoice", new_invoice_ui("new_invoice", config)),
        ui.nav_panel("Configuration", config_ui("config")),
        title="Shiny Invoice",
        id="navbar_id",
    )

    # pylint: enable=too-many-function-args

    # pylint: disable=redefined-builtin, unused-argument, no-value-for-parameter
    def server(input: Inputs, output: Outputs, session: Session):
        existing_invoices_server("existing_invoices", config)
        new_invoice_server("new_invoice", config)
        config_server("config", config)

    # pylint: enable=redefined-builtin, unused-argument, no-value-for-parameter

    app = App(app_ui, server, static_assets=config.get("paths").get("invoices_root_dir"))
    app.run(host=host, port=port)


if __name__ == "__main__":
    cli()

from create_api_app.conf.constants import PARTY

from rich.table import Table
from rich.panel import Panel


def project_table(name: str, db_type: str) -> Table:
    """Creates a printable project table showing the `name` and `db_type` selected."""
    table = Table()
    table.add_column("Project", style="magenta", justify="center")
    table.add_column("DB Type", style="green", justify="center")
    table.add_row(name, db_type)
    return table


def project_complete_panel() -> Panel:
    """Creates a printable project complete panel."""
    panel = Panel.fit(
        f"\n{PARTY} Project created successfully! {PARTY}",
        height=5,
        border_style="bright_green",
        style="bright_green",
    )
    return panel

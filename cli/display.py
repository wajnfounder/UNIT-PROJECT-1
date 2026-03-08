# Rich library used for styling CLI output
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.table import Table

# Create console instance
console = Console()


# Display system header
def show_header():

    header_text = (
        "OrgPulse\n"
        "Organizational Performance Tracking System"
    )

    console.print(
        Panel(
            Align.center(header_text),
            border_style="blue",
            expand=False
        )
    )


# Display normal information messages
def show_info(message):
    console.print(message)


# Display error messages in red
def show_error(message):
    console.print(f"[red]{message}[/red]")


# Display success messages in green
def show_success(message):
    console.print(f"[green]{message}[/green]")


# Display tables
def show_table(title, headers, rows):

    table = Table(title=title)

    for header in headers:
        table.add_column(header)

    for row in rows:
        table.add_row(*[str(item) for item in row])

    console.print(table)
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


# Show normal information message
def show_info(message):
    console.print(message)


# Show error message
def show_error(message):
    console.print(f"[bold red]Error:[/bold red] {message}")


# Show success message
def show_success(message):
    console.print(f"[bold green]{message}[/bold green]")


# Show table (for listing data)
def show_table(title, columns, rows):

    table = Table(title=title)

    # Add columns
    for column in columns:
        table.add_column(column, style="cyan")

    # Add rows
    for row in rows:
        table.add_row(*[str(item) for item in row])

    console.print(table)
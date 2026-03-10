from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.table import Table

console = Console()


# Header
def show_header():

    title = "[bold cyan]ORG PULSE CLI[/bold cyan]"
    subtitle = "[dim]Organizational Performance Tracking System[/dim]"

    header = f"{title}\n{subtitle}"

    console.print(
        Panel(
            Align.center(header),
            border_style="cyan",
            padding=(1, 8)
        )
    )


# Info message
def show_info(message):
    console.print(f"[cyan]{message}[/cyan]")


# Error message
def show_error(message):
    console.print(f"[bold red]✖ {message}[/bold red]")


# Success message
def show_success(message):
    console.print(f"[bold green]✔ {message}[/bold green]")


# Table display
def show_table(title, headers, rows):

    table = Table(
        title=f"[bold cyan]{title}[/bold cyan]",
        header_style="bold cyan",
        border_style="cyan",
        show_lines=False
    )

    for header in headers:
        table.add_column(header, style="white")

    for row in rows:
        table.add_row(*[str(item) for item in row])

    console.print(table)
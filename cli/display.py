from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def show_header():
    console.print(
        Panel(
            "Organizational Performance System CLI",
            style="bold cyan"
        )
    )


def show_success(message):
    console.print(f"[bold green]✔ {message}[/bold green]")


def show_error(message):
    console.print(f"[bold red]✖ {message}[/bold red]")


def show_info(message):
    console.print(f"[bold yellow]{message}[/bold yellow]")


def show_table(title, columns, rows):

    table = Table(title=title)

    for column in columns:
        table.add_column(column, style="cyan")

    for row in rows:
        table.add_row(*[str(item) for item in row])

    console.print(table)
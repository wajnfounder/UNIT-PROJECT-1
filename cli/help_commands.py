from cli.display import show_table
from colorama import Fore, Style


def show_help(role):

    # Admin commands
    if role == "admin":

        show_table(
            Fore.CYAN + "📁 Departments" + Style.RESET_ALL,
            ["Command", "Description"],
            [
                ("department create <name>", "Create a new department"),
                ("department list", "List all departments"),
            ]
        )

        show_table(
            Fore.CYAN + "🔄 Cycles" + Style.RESET_ALL,
            ["Command", "Description"],
            [
                ("cycle create <name>", "Create evaluation cycle"),
                ("cycle list", "List cycles"),
            ]
        )

    # Admin + Manager
    if role in ["admin", "manager"]:

        show_table(
            Fore.CYAN + "👥 Members" + Style.RESET_ALL,
            ["Command", "Description"],
            [
                ("member create <name> <role> <department_id>", "Create a new member"),
                ("member list", "List all members"),
            ]
        )

        show_table(
            Fore.CYAN + "📊 KPIs" + Style.RESET_ALL,
            ["Command", "Description"],
            [
                ("kpi create <name> <target> <weight> <type> <department_id>", "Create a KPI"),
                ("kpi list", "List KPIs"),
            ]
        )

        show_table(
            Fore.CYAN + "📈 Performance" + Style.RESET_ALL,
            ["Command", "Description"],
            [
                ("performance record <member_id> <kpi_id> <progress>", "Record KPI progress"),
                ("performance list", "List performance records"),
                ("performance ai", "AI analysis"),
            ]
        )

        show_table(
            Fore.CYAN + "📋 Tasks" + Style.RESET_ALL,
            ["Command", "Description"],
            [
                ("task add <kpi_id> <description>", "Add a new task"),
                ("task list", "List tasks"),
                ("task done <task_id>", "Mark task as completed"),
            ]
        )

    # Employee
    if role == "employee":

        show_table(
            Fore.CYAN + "📋 Tasks" + Style.RESET_ALL,
            ["Command", "Description"],
            [
                ("task add <kpi_id> <description>", "Add a new task"),
                ("task list", "List tasks"),
                ("task done <task_id>", "Mark task as completed"),
            ]
        )

        show_table(
            Fore.CYAN + "📈 Performance" + Style.RESET_ALL,
            ["Command", "Description"],
            [
                ("performance list", "List performance records"),
                ("performance ai", "AI analysis"),
            ]
        )
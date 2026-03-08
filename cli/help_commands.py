from cli.display import show_table


def show_help(role):

    if role == "admin":

        show_table(
            "Departments",
            ["Command", "Description"],
            [
                ("department create <name>", "Create a new department"),
                ("department list", "List all departments"),
            ]
        )

        show_table(
            "Members",
            ["Command", "Description"],
            [
                ("member create <name> <role> <department_id>", "Create a new member"),
                ("member list", "List all members"),
            ]
        )

        show_table(
            "KPIs",
            ["Command", "Description"],
            [
                ("kpi create <name> <target> <weight> <type> <department_id>", "Create a KPI"),
                ("kpi list", "List KPIs"),
            ]
        )

        show_table(
            "Cycles",
            ["Command", "Description"],
            [
                ("cycle create <name>", "Create evaluation cycle"),
                ("cycle list", "List cycles"),
            ]
        )

    if role in ["admin", "manager"]:

        show_table(
            "Performance",
            ["Command", "Description"],
            [
                ("performance record <member_id> <kpi_id> <cycle_id> <actual>", "Record KPI progress"),
                ("performance list", "List performance records"),
                ("performance report", "Performance statistics"),
                ("performance ai", "AI analysis"),
            ]
        )

    if role == "employee":

        show_table(
            "Performance",
            ["Command", "Description"],
            [
                ("performance record <member_id> <kpi_id> <cycle_id> <actual>", "Record KPI progress"),
                ("performance list", "List performance records"),
            ]
        )


from cli.display import show_error, show_success, show_table
from services.ai_analysis import analyze_performance
from cli.help_commands import show_help
import difflib


class CommandParser:

    def __init__(
        self,
        department_manager,
        member_manager,
        kpi_manager,
        cycle_manager,
        performance_manager,
        auth_manager
    ):
        self.department_manager = department_manager
        self.member_manager = member_manager
        self.kpi_manager = kpi_manager
        self.cycle_manager = cycle_manager
        self.performance_manager = performance_manager
        self.auth_manager = auth_manager

    def handle(self, entity, action, args):

        # Help Command
        if entity == "help":
           role = self.auth_manager.current_role
           show_help(role)
           return

        # Login Command
        elif entity == "login":

            if len(args) < 1:
                show_error("Usage: login <username>")
                return

            username = args[0]

            success = self.auth_manager.login(username)

            if success:
                show_success("Login successful")
            else:
                show_error("Invalid username")

            return

        # Department Commands 
        elif entity == "department":
            if not self.require_login():
                return

            if not self.check_permission(entity):
                return

            if action == "":
                print("Department commands:")
                print("  department create <name>")
                print("  department list")
                return

            if action == "create":

                if len(args) < 1:
                    show_error("Department name required")
                    return

                name = args[0]

                self.department_manager.create_department(name)

                show_success(f"Department '{name}' created")

            elif action == "list":

                departments = self.department_manager.list_departments()

                rows = [(d.id, d.name) for d in departments]

                show_table(
                    "Departments",
                    ["ID", "Name"],
                    rows
                )

            else:
                show_error("Unknown department command")

        # Member Commands
        elif entity == "member":

            if action == "":
                print("Member commands:")
                print("  member create <name> <role> <department_id>")
                print("  member list")
                return

            if action == "create":

                if len(args) < 3:
                    show_error("Usage: member create <name> <role> <department_id>")
                    return

                name = args[0]
                role = args[1]

                try:
                    department_id = int(args[2])
                except ValueError:
                    show_error("Department ID must be a number")
                    return

                self.member_manager.create_member(name, role, department_id)

                show_success(f"Member '{name}' created")

            elif action == "list":

                members = self.member_manager.list_members()

                rows = [(m.id, m.name, m.role) for m in members]

                show_table(
                    "Members",
                    ["ID", "Name", "Role"],
                    rows
                )

            else:
                show_error("Unknown member command")

        # KPI Commands
        elif entity == "kpi":
            if not self.require_login():
                return
          
            if not self.check_permission(entity):
                return

            if action == "":
                print("KPI commands:")
                print("  kpi create <name> <target> <weight> <type> <department_id>")
                print("  kpi list")
                return

            if action == "create":

                if len(args) < 5:
                    show_error("Usage: kpi create <name> <target> <weight> <type> <department_id>")
                    return

                name = args[0]

                try:
                    target = float(args[1])
                    weight = int(args[2])
                except ValueError:
                    show_error("Target and weight must be numbers")
                    return

                kpi_type = args[3]

                try:
                    department_id = int(args[4])
                except ValueError:
                    show_error("Department ID must be a number")
                    return

                self.kpi_manager.create_kpi(name, target, weight, kpi_type, department_id)

                show_success(f"KPI '{name}' created with target {target}")

            elif action == "list":

                kpis = self.kpi_manager.list_kpis()

                rows = [(k.id, k.name, k.target, k.weight, k.type) for k in kpis]

                show_table(
                    "KPIs",
                    ["ID", "Name", "Target", "Weight", "Type"],
                    rows
                )

            else:
                show_error("Unknown KPI command")

        # Cycle Commands
        elif entity == "cycle":

            if action == "create":

                if len(args) < 1:
                    show_error("Usage: cycle create <name>")
                    return

                name = args[0]

                cycle = self.cycle_manager.create_cycle(name)

                if cycle:
                    show_success(f"Cycle '{name}' created")
                else:
                    show_error("An active cycle already exists")

            elif action == "list":

                cycles = self.cycle_manager.list_cycles()

                rows = [(c.id, c.name, c.status) for c in cycles]

                show_table(
                    "Cycles",
                    ["ID", "Name", "Status"],
                    rows
                )

            else:
                show_error("Unknown cycle command")

        # Performance Commands
        elif entity == "performance":

            if action == "record":

                if len(args) < 4:
                    show_error("Usage: performance record <member_id> <kpi_id> <cycle_id> <actual>")
                    return

                try:
                    member_id = int(args[0])
                    kpi_id = int(args[1])
                    cycle_id = int(args[2])
                    actual = float(args[3])
                except ValueError:
                    show_error("IDs and actual value must be numbers")
                    return

                self.performance_manager.record_progress(
                    member_id,
                    kpi_id,
                    cycle_id,
                    actual
                )

                show_success("Performance recorded")

            elif action == "list":

                records = self.performance_manager.list_records()

                rows = [
                    (
                        r.id,
                        r.member_id,
                        r.kpi_id,
                        r.cycle_id,
                        r.progress
                    )
                    for r in records
                ]

                show_table(
                    "Performance Records",
                    ["ID", "Member", "KPI", "Cycle", "Progress"],
                    rows
                )

            elif action == "report":

                report = self.performance_manager.generate_report()

                if not report:
                    show_error("No performance data available")
                    return

                rows = [
                    ("Total Records", report["total_records"]),
                    ("Average Progress", report["average_progress"]),
                    ("Top Member", report["top_member"]),
                    ("Top Progress", report["top_progress"]),
                ]

                show_table(
                    "Performance Report",
                    ["Metric", "Value"],
                    rows
                )

            elif action == "ai":

                records = self.performance_manager.list_records()

                analysis = analyze_performance(records)

                show_success("AI Analysis:")
                print(analysis)

            else:
                show_error("Unknown performance command")

        # Unknown Command
        
        else:

          valid_commands = ["department", "member", "kpi", "cycle", "performance", "login", "help"]

          suggestion = difflib.get_close_matches(entity, valid_commands, n=1)

          show_error(f"Unknown command: {entity}")

        if suggestion:
         print(f"Did you mean: {suggestion[0]} ?")
from cli.display import show_error, show_success, show_table, show_info
from services.ai_analysis import analyze_performance
from cli.help_commands import show_help
import difflib


VALID_COMMANDS = [
    "department",
    "member",
    "kpi",
    "cycle",
    "performance",
    "task",
    "login",
    "help"
]


class CommandParser:

    def __init__(
        self,
        department_manager,
        member_manager,
        kpi_manager,
        cycle_manager,
        performance_manager,
        auth_manager,
        session,
        task_manager
    ):
        self.department_manager = department_manager
        self.member_manager = member_manager
        self.kpi_manager = kpi_manager
        self.cycle_manager = cycle_manager
        self.performance_manager = performance_manager
        self.auth_manager = auth_manager
        self.session = session
        self.task_manager = task_manager


    # Helpers

    def require_login(self):
        if not self.auth_manager.current_user:
            show_error("You must login first")
            return False
        return True


    def check_permission(self, entity):

        role = self.auth_manager.current_user

        permissions = {
            "admin": ["department", "member", "kpi", "cycle", "performance", "task"],
            "manager": ["member", "kpi", "performance", "task"],
            "employee": ["performance", "task"]
        }

        if entity not in permissions.get(role, []):
            show_error("Permission denied")
            return False

        return True


    def parse_int(self, value, error_message):
        try:
            return int(value)
        except ValueError:
            show_error(error_message)
            return None


    # Main handler

    def handle(self, entity, action, args):

        # HELP
        if entity == "help":
            role = self.auth_manager.current_user
            show_help(role)
            return

        # LOGIN
        elif entity == "login":

            if len(args) < 1:
                show_error("Usage: login <username>")
                return

            username = args[0]

            if self.auth_manager.login(username):
                show_success("Login successful")
            else:
                show_error("Invalid username")

            return


        # DEPARTMENT
        elif entity == "department":

            if not self.require_login() or not self.check_permission(entity):
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


        # MEMBER
        elif entity == "member":

            if not self.require_login() or not self.check_permission(entity):
                return

            if action == "create":

                if len(args) < 3:
                    show_error("Usage: member create <name> <role> <department_id>")
                    return

                name = args[0]
                role = args[1]

                department_id = self.parse_int(args[2], "Department ID must be a number")
                if department_id is None:
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


        # KPI
        elif entity == "kpi":

            if not self.require_login() or not self.check_permission(entity):
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

                department_id = self.parse_int(args[4], "Department ID must be a number")
                if department_id is None:
                    return

                self.kpi_manager.create_kpi(name, target, weight, kpi_type, department_id)
                show_success(f"KPI '{name}' created")

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


        # CYCLE
        elif entity == "cycle":

            if not self.require_login() or not self.check_permission(entity):
                return

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

            elif action == "close":
                if len(args) < 1:
                   show_error("Usage: cycle close <cycle_id>")
                   return

                cycle_id = self.parse_int(args[0], "Cycle ID must be a number")
                if cycle_id is None:
                   return

                success = self.cycle_manager.close_cycle(cycle_id)
                if success:
                   show_success("Cycle closed successfully")
                else:
                   show_error("Cycle not found")






            else:
                show_error("Unknown cycle command")


        # PERFORMANCE
        elif entity == "performance":

            if not self.require_login() or not self.check_permission(entity):
                return

            if action == "record":

                if len(args) < 3:
                    show_error("Usage: performance record <member_id> <kpi_id> <progress>")
                    return

                member_id = self.parse_int(args[0], "Member ID must be a number")
                if member_id is None:
                    return

                kpi_id = self.parse_int(args[1], "KPI ID must be a number")
                if kpi_id is None:
                    return

                progress = self.parse_int(args[2], "Progress must be a number")
                if progress is None:
                    return

                active_cycle = self.cycle_manager.get_active_cycle()

                if not active_cycle:
                    show_error("No active cycle found")
                    return

                self.performance_manager.record_progress(
                    member_id,
                    kpi_id,
                    active_cycle.id,
                    progress
                )

                show_success("Performance recorded successfully")

            elif action == "list":

                records = self.performance_manager.list_records()

                rows = [
                    (r.id, r.member_id, r.kpi_id, r.cycle_id, r.progress)
                    for r in records
                ]

                show_table(
                    "Performance Records",
                    ["ID", "Member", "KPI", "Cycle", "Progress"],
                    rows
                )

            elif action == "ai":

                records = self.performance_manager.list_records()

                analysis = analyze_performance(records)

                show_success("AI Analysis:")
                print(analysis)

            else:
                show_error("Unknown performance command")


        # TASK
        elif entity == "task":

            if not self.require_login() or not self.check_permission(entity):
                return

            self.handle_task(action, args)


        # UNKNOWN
        else:

            show_error(f"Unknown command: {entity}")

            suggestion = difflib.get_close_matches(entity, VALID_COMMANDS, n=1)

            if suggestion:
                print(f"Did you mean: {suggestion[0]} ?")


    # TASK HANDLER
    def handle_task(self, action, args):

        if action == "add":

            if len(args) == 0:
                show_info("Please choose a KPI first\n")

                kpis = self.kpi_manager.list_kpis()

                rows = [(k.id, k.name, k.target) for k in kpis]

                show_table(
                    "Available KPIs",
                    ["ID", "Name", "Target"],
                    rows
                )
                return

            if len(args) < 2:
                show_error("Usage: task add <kpi_id> <description>")
                return

            kpi_id = self.parse_int(args[0], "KPI ID must be a number")
            if kpi_id is None:
                return

            description = " ".join(args[1:])
            member_id = self.auth_manager.current_user

            self.task_manager.add_task(member_id, kpi_id, description)

            show_success("Task added successfully")


        elif action == "done":

            if len(args) < 1:
                show_error("Usage: task done <task_id>")
                return

            task_id = self.parse_int(args[0], "Task ID must be a number")
            if task_id is None:
                return

            progress = self.task_manager.complete_task(task_id)

            if progress is None:
                show_error("Task not found")
                return

            show_success("Task marked as completed")
            show_success(f"Updated KPI progress: {progress}%")
            self.show_progress_bar(progress)


        elif action == "list":

            role = self.auth_manager.current_user

            if role == "employee":
                tasks = self.task_manager.get_number_tasks(role)
            else:
                tasks = self.task_manager.list_tasks()

            rows = [
                (t["id"], t["member_id"], t["kpi_id"], t["description"], t["status"])
                for t in tasks
            ]

            show_table(
                "Tasks",
                ["ID", "Member", "KPI", "Description", "Status"],
                rows
            )

        else:
            show_error("Unknown task command")


    def show_progress_bar(self, progress):

        bar_length = 20
        filled = int(bar_length * progress / 100)

        bar = "█" * filled + "░" * (bar_length - filled)

        print(f"\nProgress:\n[{bar}] {progress}%\n")
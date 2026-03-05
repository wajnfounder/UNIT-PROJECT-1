from cli.display import show_error, show_success, show_table


class CommandParser:

    def __init__(self, department_manager, member_manager, kpi_manager, cycle_manager, performance_manager):
        self.department_manager = department_manager
        self.member_manager = member_manager
        self.kpi_manager = kpi_manager
        self.cycle_manager = cycle_manager
        self.performance_manager = performance_manager


    def handle(self, entity, action, args):

        if entity == "department":

            if action == "create":

                if len(args) < 1:
                    show_error("Department name required")
                    return

                name = args[0]

                department = self.department_manager.create_department(name)

                show_success(f"Department '{name}' created")


            elif action == "list":

                departments = self.department_manager.list_departments()

                rows = [(d.id, d.name) for d in departments]

                show_table("Departments", ["ID", "Name"], rows)


            else:
                show_error("Unknown department command")


        elif entity == "member":

            if action == "create":

                if len(args) < 3:
                    show_error("Usage: member create <name> <role> <department_id>")
                    return

                name = args[0]
                role = args[1]
                department_id = int(args[2])

                member = self.member_manager.create_member(name, role, department_id)

                show_success(f"Member '{name}' created")


            elif action == "list":

                members = self.member_manager.list_members()

                rows = [(m.id, m.name, m.role) for m in members]

                show_table("Members", ["ID", "Name", "Role"], rows)


            else:
                show_error("Unknown member command")


        else:
            show_error("Unknown command")
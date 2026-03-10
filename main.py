from managers.storage_manager import StorageManager
from managers.department_manager import DepartmentManager
from managers.member_manager import MemberManager
from managers.kpi_manager import KPIManager
from managers.cycle_manager import CycleManager
from managers.performance_manager import PerformanceManager
from managers.authorization_manager import AuthorizationManager
from managers.task_manager import TaskManager

from cli.command_parser import CommandParser
from cli.shell import start_shell
from cli.session import Session


def main():

    # Storage
    storage = StorageManager()

    # Session
    session = Session()

    # Managers
    department_manager = DepartmentManager(storage)
    member_manager = MemberManager(storage)
    kpi_manager = KPIManager(storage)
    cycle_manager = CycleManager(storage)
    task_manager = TaskManager(storage)
    performance_manager = PerformanceManager(storage, kpi_manager)

    # Authorization
    auth_manager = AuthorizationManager()

    # Command Parser
    parser = CommandParser(
        department_manager,
        member_manager,
        kpi_manager,
        cycle_manager,
        performance_manager,
        auth_manager,
        session,
        task_manager
    )

    # Start CLI
    start_shell(parser)


if __name__ == "__main__":
    main()
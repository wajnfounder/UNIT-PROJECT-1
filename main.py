# Import managers responsible for handling different entities
from managers.storage_manager import StorageManager
from managers.department_manager import DepartmentManager
from managers.member_manager import MemberManager
from managers.kpi_manager import KPIManager
from managers.cycle_manager import CycleManager
from managers.performance_manager import PerformanceManager

# Import CLI components
from cli.session import Session
from cli.command_parser import CommandParser
from cli.shell import start_shell


def main():

    # Initialize storage system
    storage = StorageManager()

    # Initialize managers and pass storage dependency
    department_manager = DepartmentManager(storage)
    member_manager = MemberManager(storage)
    kpi_manager = KPIManager(storage)
    cycle_manager = CycleManager(storage)
    performance_manager = PerformanceManager(storage)

    # Create a session object to track logged-in user
    session = Session()

    # Initialize command parser with all managers
    parser = CommandParser(
        department_manager,
        member_manager,
        kpi_manager,
        cycle_manager,
        performance_manager
    )

    # Start the CLI
    start_shell(parser, session)


# Run the program
if __name__ == "__main__":
    main()
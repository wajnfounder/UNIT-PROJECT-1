# Import display helpers
from cli.display import show_header, show_error, show_info

# Import command parser helper
from cli.input_handler import parse_input


def start_shell(parser, session):

    # Display system header
    show_header()

    
    show_info("Welcome to OrgPulse!")
    show_info("Type 'help' to see available commands\n")

    # Main CLI loop
    while True:

        # Get current user from session
        username = session.get_username()

        # Build command prompt
        if username:
            prompt = f"orgpulse({username}) > "
        else:
            prompt = "orgpulse > "

        # Read user command
        command = input(prompt).strip()

        # Ignore empty input
        if command == "":
            continue

        # Exit command
        if command == "exit":
            print("Goodbye good to see you!")
            break

        # Parse command into entity, action, and arguments
        entity, action, args = parse_input(command)

        # Handle invalid commands
        if entity is None:
            show_error("Invalid command")
            continue

        # Send command to parser
        parser.handle(entity, action, args)
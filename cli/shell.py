from cli.display import show_header, show_error
from cli.input_handler import parse_input


def start_shell(parser, session):

    show_header()

    while True:

        username = session.get_username()

        if username:
            prompt = f"orgpulse({username}) > "
        else:
            prompt = "orgpulse > "

        command = input(prompt).strip()

        if command == "":
            continue

        if command == "exit":
            print("Goodbye 👋")
            break

        entity, action, args = parse_input(command)

        if entity is None:
            show_error("Invalid command")
            continue

        parser.handle(entity, action, args)
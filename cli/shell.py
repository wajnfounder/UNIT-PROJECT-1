from cli.display import show_header, show_info, show_table
import difflib


def start_shell(parser, session):

    roles = ["admin", "manager", "employee"]

    show_header()
    show_info("Welcome to OrgPulse!\n")

    print("Available roles:")
    print("  admin")
    print("  manager")
    print("  employee\n")

    print("Please login with your role to continue\n")

    # Login loop
    while True:
        try:
            username = input("Username: ").strip().lower()

            if username == "":
                continue

            if username in roles:
                parser.auth_manager.login(username)
                print(f"\nLogin successful ({username})\n")

                show_table(
                    "Quick Commands",
                    ["Command", "Description"],
                    [
                        ("help", "Show commands"),
                        ("exit", "Exit system")
                    ]
                )

                break

            suggestion = difflib.get_close_matches(username, roles, n=1)

            if suggestion:
                print(f"Invalid username. Did you mean: {suggestion[0]} ?\n")
            else:
                print("Invalid username, try again.\n")

        except KeyboardInterrupt:
            print("\nUse 'exit' to quit.")
            continue

    # CLI loop
    while True:
        try:
            prompt = f"{parser.auth_manager.current_user}@orgpulse > "
            command = input(prompt).strip()

            if command == "":
                continue

            # ignore VS Code auto commands
            if command.startswith("&") or "python.exe" in command:
                continue

            if command.lower() == "exit":
                print("Exiting OrgPulse...")
                break

            if command.lower() == "help":
                parser.handle("help", "", [])
                continue

            parts = command.split()

            entity = parts[0]
            action = parts[1] if len(parts) > 1 else ""
            args = parts[2:] if len(parts) > 2 else []

            parser.handle(entity, action, args)

        except KeyboardInterrupt:
            print("\nUse 'exit' to quit.")
            continue

        except Exception:
            continue
        
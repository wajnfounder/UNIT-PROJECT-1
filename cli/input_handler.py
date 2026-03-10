import shlex


# Parse user input from CLI into entity, action, and arguments
def parse_input(command):

    try:
        parts = shlex.split(command)

        if not parts:
            return None, None, []

        entity = parts[0]
        action = parts[1] if len(parts) > 1 else ""
        args = parts[2:] if len(parts) > 2 else []

        return entity, action, args

    except ValueError:
        # Handle malformed input (e.g., unclosed quotes)
        return None, None, []
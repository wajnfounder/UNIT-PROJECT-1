import shlex


def parse_input(command):

    try:
        parts = shlex.split(command)

        if len(parts) == 0:
            return None, None, []

        entity = parts[0]

        action = parts[1] if len(parts) > 1 else None

        args = parts[2:] if len(parts) > 2 else []

        return entity, action, args

    except ValueError:
        return None, None, []
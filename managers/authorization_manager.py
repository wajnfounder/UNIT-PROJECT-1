class AuthorizationManager:

    def __init__(self):
        self.current_user = None
        self.current_role = None

    def login(self, username):

        roles = {
            "admin": "admin",
            "manager": "manager",
            "employee": "employee"
        }

        if username in roles:
            self.current_user = username
            self.current_role = roles[username]
            return True

        return False
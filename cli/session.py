class Session:

    # Stores the current logged-in user
    def __init__(self):
        self.current_user = None

    # Set the active user in the session
    def login(self, member):
        self.current_user = member

    # Clear the session
    def logout(self):
        self.current_user = None

    # Check if a user is logged in
    def is_logged_in(self):
        return self.current_user is not None

    # Return the current user object
    def get_current_user(self):
        return self.current_user

    # Return username safely
    def get_username(self):
        return self.current_user.name if self.current_user else None
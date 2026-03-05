class Session:

    def __init__(self):
        self.current_user = None


    def login(self, member):
        self.current_user = member


    def logout(self):
        self.current_user = None


    def is_logged_in(self):
        return self.current_user is not None


    def get_current_user(self):
        return self.current_user


    def get_username(self):
        if self.current_user:
            return self.current_user.name
        return None
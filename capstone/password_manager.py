class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def add_password(self, site, password):
        self.passwords[site] = password

    def get_password(self, site):
        return self.passwords.get(site)

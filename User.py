from Library import Library


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bought_books = []

        if len(Library.users) == 0:
            self.role = "admin"
        else:
            self.role = "user"

    def __str__(self):
        return f"({self.username}, {self.password}, {self.role})"



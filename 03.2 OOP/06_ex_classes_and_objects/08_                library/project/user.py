class User:

    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def info(self):
        pass

    def __str__(self):
        rented_books = ', '.join(el for el in self.books)
        return f"{self.user_id}, {self.username} {rented_books}"


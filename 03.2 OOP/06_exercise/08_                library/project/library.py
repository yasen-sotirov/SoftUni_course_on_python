from project.user import User

class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author:str, book_name: str, days_to_return: int, user: User):
        for el in self.books_available:
            if book_name == self.books_available.name
class LibraryManager:
    def __init__(self):
        self.books = {}

    def add_book(self, title, count=1):
        self.books[title] = self.books.get(title, 0) + count

    def borrow_book(self, title):
        if self.books.get(title, 0) > 0:
            self.books[title] -= 1
            return True
        return False

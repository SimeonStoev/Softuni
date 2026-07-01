from project.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def is_book_available(self, author, book):
        return author in self.books_available and book in self.books_available[author]

    def get_return_days(self, book_name):
        for user_books in self.rented_books.values():
            if book_name in user_books:
                return user_books[book_name]
        return 0

    def is_book_rented(self, username, book_name):
        return username in self.rented_books and book_name in self.rented_books[username]

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if self.is_book_available(author, book_name):
            # add the book to the rented books
            if user.username not in self.rented_books:
                self.rented_books[user.username] = {}
            self.rented_books[user.username][book_name] = days_to_return
            # add the book to user book list
            user.books.append(book_name)
            # remove book from available books
            self.books_available[author].remove(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        return f'The book "{book_name}" is already rented and will be available in {self.get_return_days(book_name)} days!'

    def return_book(self, author: str, book_name: str, user: User):
        if book_name in user.books and self.is_book_rented(user.username, book_name):
            user.books.remove(book_name)
            del self.rented_books[user.username][book_name]
            if author not in self.books_available:
                self.books_available[author] = []
            self.books_available[author].append(book_name)
            return None
        else:
            return f"{user.username} doesn't have this book in his/her records!"

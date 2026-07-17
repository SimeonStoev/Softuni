class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Page: {self.page}"

class Library:
    def __init__(self, location):
        self.location = location
        self.books = []

    def find_book(self, title):
        try:
            book = [book for book in self.books if book.title == title][0]
            return book
        except IndexError:
            return f"No book found for {title}"

b1 = Book("Book 1", "Dan one")
b2 = Book("Book 2", "Dan two")
b3 = Book("Book 3", "Dan three")

library = Library("Sofia")
library.books.append(b1)
library.books.append(b2)
library.books.append(b3)

print(library.find_book("Book 1"))
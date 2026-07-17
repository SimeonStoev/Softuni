class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    def format(self, book: Book) -> str:
        return book.content


class Printer:
    def get_book(self, book: Book, formatter: Formatter) -> str:
        return formatter.format(book)


book1 = Book("one")
book2 = Book("two")

formater = Formatter()

printer = Printer()

print(printer.get_book(book1, formater))
print(printer.get_book(book2, formater))

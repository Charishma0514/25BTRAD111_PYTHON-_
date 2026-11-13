class Book:
    def __init__(self, title):
        self.title = title
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added:", book.title)

    def issue_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.available:
                    book.available = False
                    print("Book issued successfully")
                else:
                    print("Book is not available")
                return
        print("Book not found")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.available:
                    book.available = True
                    print("Book returned successfully")
                else:
                    print("Book was not issued")
                return
        print("Book not found")

    def display_books(self):
        for book in self.books:
            if book.available:
                print(book.title, "- Available")
            else:
                print(book.title, "- Issued")


library = Library()

b1 = Book("Python")
b2 = Book("Java")

library.add_book(b1)
library.add_book(b2)

library.display_books()

library.issue_book("Python")
library.display_books()

library.return_book("Python")
library.display_books()

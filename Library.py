class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        return f"'{self.title}' by {self.author} - {'Available' if self.available else 'Not Available'}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print(f"You have borrowed '{title}'")
                return
        print(f"'{title}' is not available or doesn't exist in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                print(f"'{title}' has been returned to the library.")
                return
        print(f"'{title}' is not recognized as borrowed.")

    def display_books(self):
        print("\nLibrary Collection:")
        for book in self.books:
            print(book)


# Example usage
library = Library()

# Adding books
library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))

# Displaying books
library.display_books()

# Borrowing a book
library.borrow_book("1984")
library.display_books()

# Returning a book
library.return_book("1984")
library.display_books()

# Attempting to borrow a non-existent book
library.borrow_book("Moby Dick")

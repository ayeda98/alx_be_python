class Book:
    def __init__(self, title, author):
        self.title = title                 # Public attribute
        self.author = author               # Public attribute
        self._is_checked_out = False       # Private attribute

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as available."""
        self._is_checked_out = False

    def is_checked_out(self):
        """Check if the book is checked out."""
        return self._is_checked_out

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title."""
        for book in self._books:
            if book.title == title and not book.is_checked_out():
                book.check_out()
                print(f"{title} has been checked out.")
                return
        print(f"{title} is not available for checkout.")

    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title and book.is_checked_out():
                book.return_book()
                print(f"{title} has been returned.")
                return
        print(f"{title} was not checked out.")

    def list_available_books(self):
        """Display all available books in the library."""
        available_books = [str(book) for book in self._books if not book.is_checked_out()]
        if not available_books:
            print("No books are currently available.")
        else:
            print("Available books:")
            for book in available_books:
                print(book)

# Principal class
class Book:
    def __init__(self, title, author, year=None):
        self.title = title 
        self.author = author
        self.year = year 

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
    
    def __str__(self):
        return f"Book: {self.title} by {self.author}"


# Sous-classe pour les eBooks
class EBook(Book):
    def __init__(self, title, author, file_size, year=None):
        super().__init__(title, author, year)  
        self.file_size = file_size

    def __str__(self):
        return f" EBook: {self.title} by {self.author}, published in {self.year}, size: {self.file_size}KB"


# Sous-classe pour les livres imprimés
class PrintBook(Book):
    def __init__(self, title, author, page_count, year=None):
        super().__init__(title, author, year)  
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, published in {self.year}, {self.page_count} pages"


# Classe Bibliothèque
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(str(book))


# Exemple d'utilisation
library = Library()

# Ajout des livres
library.add_book(Book("Pride and Prejudice", "Jane Austen"))
library.add_book(EBook("Snow Crash", "Neal Stephenson", 500))
library.add_book(PrintBook("The Catcher in the Rye", "J.D. Salinger", 234))

# Affichage de la liste des livres
library.list_books()
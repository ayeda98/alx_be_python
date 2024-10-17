class VoitureDeCourse(Voiture):  # Hérite de la classe Voiture
    def __init__(self, couleur, marque, vitesse_max):
        super().__init__(couleur, marque)  # Appelle le constructeur de la classe parente
        self.vitesse_max = vitesse_max  # Attribut spécifique à VoitureDeCourse

#principal class
class Book:
    def __init__(self, title, author):
        self.titel = title
        self.author = author

#
class EBook(Book):
    def __init__(self, title, author, size):
        super().__init__(title, author)
        self.size = size

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book)
            self.books.append(book)

  
    def List_book(self):
        for book in self.books:
            print(book)


class Book:
    def __init__(self, title, author, is_checked_out):
        self.title = title 
        self.author = author 
        self.__is_checked_out = is_checked_out

    def get_title(self):
        return self.title

    def is_checked_out(self):
        return self.__is_checked_out


class Library:
    def __init__(self, list_books):
        self.__list_books = list(list_books)
    
    def check_out_book(self, book):
        if book in self.__list_books:
            self.__list_books.remove(book)
            print(f"{book.get_title()} has been checked out.")
        else:
            print(f"{book.get_title()} is not available in the library.")
    
    def add_book(self, book):
        self.__list_books.append(book)
        print(f"{book.get_title()} has been added to the library.")

    def list_available_books(self):
        if not self.__list_books:
            print("No books available in the library.")
        else:
            print("Available books in the library:")
            for book in self.__list_books:
                print(book.get_title())

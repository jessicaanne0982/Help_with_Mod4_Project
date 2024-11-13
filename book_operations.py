
class Books:
    def __init__(self, title, author, genre, pub_date):
        self.title = title
        self.author = author
        self.genre = genre
        self.pub_date = pub_date
        self.availability = True

    def lend_book(self):
        if self.availability:
            self.availability = False
            return True
        return False

    def return_book(self):
        self.availability = True

class BookOperations:
    def __init__(self):
        self.library_catalog = []

    def add_book_to_library(self, book):
        self.library_catalog.append(book)

    def search_catalog(self, title):
        for book in self.library_catalog:
            if book.title == title:
                return book
        return None
    
    def checkout(self, title):
        book = self.search_catalog(title)
        if book and book.lend_book():
            print(f"{title} has been checked out")
            return True
        else:
            print(f"{title} is not available to borrow currently")
            return False

    def return_book(self, title):
        book = self.search_catalog(title)
        if book:
            book.return_book()
            print(f"{title} has been returned to the library and is available to checkout")
        else:
            print(f"{title} not found in the library catalog")

    def display_books(self): 
        for book in self.library_catalog:
            print(f"\nTitle: {book.title} \nAuthor: {book.author}" 
                  f"\nGenre: {book.genre} \nPublication Date: {book.pub_date}")

    def export_books_to_file(self, filename):
        with open(filename, 'a') as file:
            for book in self.library_catalog:
                file.write(f"\nTitle: {book.title} \nAuthor: {book.author} \nGenre: {book.genre}"
                           f"\nPublication Year: {book.pub_date}\n")
            print("Book catalog successfully exported to 'book_catalog.txt'")
            
  

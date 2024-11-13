class LibraryPatron:
    def __init__(self, name, library_id):
        self.name = name
        self.__library_id = library_id
        self.borrowed_books = []

    def get_library_id(self):
        return self.__library_id
    
    def set_library_id(self, protected_id):
        self.__library_id = protected_id

    def borrow_book(self, book_title):
        self.borrowed_books.append(book_title)

    def list_borrowed_books(self):
        return self.borrowed_books

class PatronOperations:
    def __init__(self):
        self.patron_list = [] 

    def add_patron(self, patron):
        self.patron_list.append(patron) 

    def search_for_patron(self, name):
        for patron in self.patron_list:
            if patron.name == name:
                return patron
        return None   

    def display_all_patrons(self):  
        for patron in self.patron_list:
            print(f"\nName: {patron.name} \nLibrary ID: ******{patron.get_library_id()[6:]}"
                  f"\nBorrowed Books: {patron.list_borrowed_books()}") 
            
    def export_patrons_to_file(self, filename):
        with open(filename, 'a') as file:
            for patron in self.patron_list:
                file.write(f"\nName: {patron.name} \nLibrary ID: ******{patron.get_library_id()[6:]}"
                            f"\nBooks borrowed: {patron.list_borrowed_books()}?\n")
            print("Patron list successfully exported to 'patron_details.txt'")

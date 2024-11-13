from book_operations import Books, BookOperations
from patron_operations import LibraryPatron, PatronOperations
from author_operations import Authors, AuthorOperations
import re


catalog = BookOperations()
patron_list = PatronOperations()
author_list = AuthorOperations()

def main():
    print("Welcome to the Library Management System!")
    while True:
        main_menu_action = input("\nChoose from the following options: "
                                    "\n1. Book Operations"
                                    "\n2. Patron Operations"
                                    "\n3. Author Operations"
                                    "\n4. Quit"
                                    "\n")
        if main_menu_action == '4':
            print("Thank you for using the Library Management System! \nExiting now...")
            break
        try:
            if main_menu_action == '1':
                book_menu_option = input("Book Operations Menu: \nPlease choose from the following options:"
                    "\n1. Add a new book"
                    "\n2. Borrow a book"
                    "\n3. Return a book"
                    "\n4. Search for a book"
                    "\n5. Display all books"
                    "\n6. Export book catalog to a text file"
                    "\n")
                try:
                    if book_menu_option == '1':
                        title = input("Enter the name of the book to add: ")
                        author = input("Enter the book's author: ")
                        genre = input("Enter the book's genre: ")
                        pub_date = input("Enter the publication year: ")
                        catalog.add_book_to_library(Books(title, author, genre, pub_date))
                        print(f"{title} has been added to the Library Catalog.")
                    elif book_menu_option == '2':
                        borrower_name = input("Enter the name of the patron borrowing the book: ") 
                        borrower = patron_list.search_for_patron(borrower_name)
                        if borrower:
                            title = input("Enter the title of the book to borrow: ")
                            if catalog.checkout(title): 
                                borrower.borrow_book(title)
                                print(f"{title} has been successfully borrowed by {borrower_name}")
                        else:
                            print("This patron was not found in the library system.")                               
                    elif book_menu_option == '3':
                        title = input("Enter the title of the book to return: ")
                        catalog.return_book(title)
                    elif book_menu_option == '4':
                        title = input("Enter the name of the book to search: ")
                        book = catalog.search_catalog(title)
                        if book:
                            available = "available" if book.availability else "not available"
                            print(f"{title} by {book.author} is {available}")
                        else:
                            print(f"{title} was not found")
                    elif book_menu_option == '5':
                        catalog.display_books()
                    elif book_menu_option == '6':
                        catalog.export_books_to_file('book_catalog.txt')
                except ValueError:
                    print("Invalid option.  Enter a number 1 - 6: ")
            elif main_menu_action == '2':
                patron_menu_option = input("Patron Operations Menu: \nPlease choose from the following options:"
                      "\n1. Add a new patron"
                      "\n2. View patron details"
                      "\n3. Display all patrons"
                      "\n4. Export patron list to a text file"
                      "\n")
                try:
                    if patron_menu_option == '1':
                        name = input("Enter the patron's first and last name: ")
                        library_id = input("Enter the patron's 10 digit ID number: ")
                        if not re.search(r"\d{10}", library_id):
                            print("Invalid Library ID number.  The ID should be 10 digits in length.")
                        else:
                            patron_list.add_patron(LibraryPatron(name, library_id))
                            print(f"{name} has been added to the list of Library Patrons")
                    elif patron_menu_option == '2':
                        name = input("Enter the patron's name to search: ")
                        patron = patron_list.search_for_patron(name)
                        if patron:
                            print(f"Patron details: \nName: {name} \nLibrary ID: ******{patron.get_library_id()[6:]}"
                                f"\nBorrowed Books: {patron.list_borrowed_books()}") 
                        else:
                            print(f"{name} was not found in the Patron List.")
                    elif patron_menu_option == '3':
                        patron_list.display_all_patrons()
                    elif patron_menu_option == '4':
                        patron_list.export_patrons_to_file('patron_details.txt')
                except ValueError:
                    print("Invalid option.  Enter a number 1 - 4: ")

            elif main_menu_action == '3':
                author_menu_option = input("Author Operations Menu: \nPlease choose from the following options:"
                      "\n1. Add a new author"
                      "\n2. View author details"
                      "\n3. Display all authors"
                      "\n4. Export author details to a text file"
                      "\n")
                try:
                    if author_menu_option == '1':
                        name = input("Enter the author's first and last name: ")
                        biography = input("Enter a short biography of the author: ")
                        author_list.add_author(Authors(name, biography))
                        print(f"The author, {name}, has been added to the list")
                    elif author_menu_option == '2':
                        name = input("Enter the author's name to search: ")
                        author = author_list.search_for_author(name)
                        if author:
                            print(f"Author details: \nName: {name} \nBiography: {author.biography}")
                        else:
                            print(f"{name} was not found in the Author List.")
                    elif author_menu_option == '3':
                        author_list.display_all_authors()
                    elif author_menu_option == '4':
                        author_list.export_authors_to_file('author_details.txt')
                except ValueError:
                    print("Invalid option.  Enter a number 1 - 4: ")
        except ValueError:
            print("Invalid option.  Enter a number 1 - 4: ")

if __name__ == "__main__":
    main()
            
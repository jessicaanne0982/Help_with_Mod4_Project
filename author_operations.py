class Authors:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

class AuthorOperations:
    def __init__(self):
        self.author_list = []  

    def add_author(self, author):
        self.author_list.append(author) 

    def search_for_author(self, name):
        for author in self.author_list:
            if author.name == name:
                return author
        return None   

    def display_all_authors(self):  
        for author in self.author_list:
            print(f"\nName: {author.name} \nBiography: {author.biography}")

    def export_authors_to_file(self, filename):
        with open(filename, 'a') as file:
            for author in self.author_list:
                file.write(f"\nName: {author.name} \nBiography: {author.biography}\n")
            print("Author details successfully exported to 'author_details.txt'")
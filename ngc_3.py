
class book:
    """
    Represents a book with its title, author, and unique identifier.
    This class provides a simple way to model book information. 

    Args:
        title (str): The title of the book. Defaults to an empty string.
        author (str): The author of the book. Defaults to an empty string.
        id (str): A unique identifier for the book. Defaults to an empty string.nb/
    """
    def __init__(self,title=str, author=str, id=str):
        self.title = title
        self.author = author
        self.id = id


class library:
    """
    A class representing a library catalog that stores and manages Book objects.

    This class provides functionalities to add, search, remove, and view books within the library catalog.
    """
    def __init__(self):
        self.catalog = []

    def add_book(self, book_item=book):
        '''
        function to add book to attribute catalog

        args:
            book_item (book): object from class book to be put in catalog
        '''
        self.catalog.append(book_item)

    def search_book(self, search=str):
        '''
        method to find books in catalog based on title or author by search keyword

        args:
            search (str): keyword to find book that have the same word in book title or author
                     from catalog
        
        return:
            result (list): list of book that match search keyword
        '''
        result = []
        if len(self.catalog) < 1:
            print('library is currently empty')
        
        else:
            for i in self.catalog:
                if search in i.title.lower() or search in i.author.lower():
                    result.append(i)
                
            return result

    def remove_book(self, search=str):
        '''
        method to remove books from catalog based on title by search keyword

        args:
            search (str): keyword to find and remove book that have the same word in 
                          book title from catalog
        '''
        if len(self.catalog) < 1:
            print('library is currently empty')
        
        else:
            for i in self.catalog:
                if search in i.title.lower():
                    self.catalog.remove(i)
                    print(f'{search} removed from catalog')
                else:
                    print('Book not found')
    
    def view_catalog(self):
        '''
        method to show catalog items
        '''
        if len(self.catalog) < 1:
            print('library is currently empty')
        
        else:
            print('No. |     Title     |     Author     |   ID   |')
            for i in range(len(self.catalog)):
                print(f'{i+1} | {self.catalog[i].title} | {self.catalog[i].author} | {self.catalog[i].id} |')
            

def libraryMenu(lib_object=library):
    '''
    function to display interface of library
    
    args:
        lib_object (library): object of class library
    '''
    while True:
        print(
'''
================================
  Hacktiv8 Library
================================

Menu:
1. View Catalog
2. Add Book
3. Search Book
4. Remove Book

type 'exit' to quit
''')
        menu = input('Input menu number or exit: ')

        if menu == '1':
            lib_object.view_catalog()
        
        elif menu == '2':
            print()
            print('------Book Input------')
            print()
            bookName = input("Book name: ")
            bookAuth = input('Book author: ')
            bookId = (input('Book ID: '))
            putBook = book(bookName, bookAuth, bookId)
            lib_object.add_book(putBook)
        
        elif menu == '3':
            print()
            print('------Book Search------')
            print()
            find = input('Book title or author: ').lower()
            print('----------------------')
            result = lib_object.search_book(find)
            for i in result:
                print(f'Title: {i.title}')
                print(f'Author: {i.author}')
                print(f'ID: {i.id}')
                print('----------------------')
        
        elif menu == '4':
            print()
            print('------Remove Book------')
            print()
            find = input('Book title to remove: ').lower()
            lib_object.remove_book(find)

        elif menu.lower() == 'exit':
            print('See you next time')
            break

        else:
            print('WRONG INPUT, TRY AGAIN')


if __name__ == '__main__':
    # Create an instance of the LibraryCatalog
    library_catalog = library()

    # Add some books to the catalog
    book1 = book("Python for Beginners", "John Smith", 1)
    book2 = book("Data Science 101", "Jane Doe", 2)
    book3 = book("Web Development Basics", "John Smith", 3)

    library_catalog.add_book(book1)
    library_catalog.add_book(book2)
    library_catalog.add_book(book3)

    # run menu
    libraryMenu(library_catalog)
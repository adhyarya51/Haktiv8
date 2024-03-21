import unittest

#import class book dan library dari modul ngc_3
from ngc_3 import book, library 

class LibraryCatalogTests(unittest.TestCase):
    def setUp(self):
        self.lib = library()

        # Add some books to the catalog
        book1 = book("Python for Beginners", "John Smith", 1)
        book2 = book("Data Science 101", "Jane Doe", 2)
        book3 = book("Web Development Basics", "John Smith", 3)

        self.lib.add_book(book1)
        self.lib.add_book(book2)
        self.lib.add_book(book3) # seharusnya sampai sini isi catalog ada 3

    def testAddCase1(self):
        book4 = book("Python pandas with real panda", 'Po', 4)
        self.lib.add_book(book4) # tambah 1 buku
        self.assertEqual(len(self.lib.catalog), 4) # seharusnya len dari list catalog jadi 4

    def testAddCase2(self):
        book5 = book("Unit testing for babies", 'Vincent', 5)
        book4 = book("Python pandas with real panda", 'Po', 4)
        self.lib.add_book(book4)
        self.lib.add_book(book5) # tambah 2 buku
        self.assertEqual(len(self.lib.catalog), 5) # seharusnya len dari list katalog jadi 5

    def testRemove(self):
        self.lib.remove_book('data science 101') # kurangi 1 buku
        self.assertEqual(len(self.lib.catalog), 2) # seharusnya jadi 2



if __name__ == '__main__':
    unittest.main()
        
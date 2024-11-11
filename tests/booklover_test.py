import unittest
from booklover.booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        book_lover_instance = BookLover("Test User", "test@gmail.com", "fiction")
        book_lover_instance.add_book("Test Book", 4)
        self.assertTrue(book_lover_instance.has_read("Test Book"))

    def test_2_add_book(self):
        book_lover_instance = BookLover("Test User", "test@gmail.com", "fiction")
        book_lover_instance.add_book("Test Book", 4)
        book_lover_instance.add_book("Test Book", 5)
        self.assertEqual(book_lover_instance.num_books_read(), 1)

    def test_3_has_read(self):
        book_lover_instance = BookLover("Test User", "test@gmail.com", "fiction")
        book_lover_instance.add_book("Test Book", 4)
        self.assertTrue(book_lover_instance.has_read("Test Book"))

    def test_4_has_read(self):
        book_lover_instance = BookLover("Test User", "test@gmail.com", "fiction")
        book_lover_instance.add_book("Test Book", 4)
        self.assertFalse(book_lover_instance.has_read("Nonexistent Book"))

    def test_5_num_books_read(self):
        book_lover_instance = BookLover("Test User", "test@gmail.com", "fiction")
        book_lover_instance.add_book("Test Book 1", 4)
        book_lover_instance.add_book("Test Book 2", 5)
        self.assertEqual(book_lover_instance.num_books_read(), 2)

    def test_6_fav_books(self):
        book_lover_instance = BookLover("Test User", "test@gmail.com", "fiction")
        book_lover_instance.add_book("Test Book 1", 4)
        book_lover_instance.add_book("Test Book 2", 2)
        book_lover_instance.add_book("Test Book 3", 5)
        fav_books = book_lover_instance.fav_books()
        self.assertTrue(all(rating > 3 for rating in fav_books['book_rating']))

if __name__ == '__main__':
    unittest.main(verbosity=3)
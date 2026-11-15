
import unittest

from book import Book
from book_manager import BookManager


class TestBook(unittest.TestCase):

    def test_create_book(self):
        book = Book("ვეფხისტყაოსანი", "შოთა რუსთაველი", 1712)

        self.assertEqual(book.title, "ვეფხისტყაოსანი")
        self.assertEqual(book.author, "შოთა რუსთაველი")
        self.assertEqual(book.year, 1712)

    def test_empty_title(self):
        with self.assertRaises(ValueError):
            Book("", "შოთა რუსთაველი", 1712)

    def test_empty_author(self):
        with self.assertRaises(ValueError):
            Book("ვეფხისტყაოსანი", "", 1712)

    def test_invalid_year(self):
        with self.assertRaises(ValueError):
            Book("Book", "Author", 0)


class TestBookManager(unittest.TestCase):

    def setUp(self):
        self.manager = BookManager()
        self.book = Book("ვეფხისტყაოსანი", "შოთა რუსთაველი", 1712)

    def test_add_book(self):
        self.manager.add_book(self.book)

        self.assertEqual(len(self.manager.get_all_books()), 1)

    def test_get_all_books(self):
        self.manager.add_book(self.book)

        books = self.manager.get_all_books()

        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, "ვეფხისტყაოსანი")

    def test_search_book(self):
        self.manager.add_book(self.book)

        result = self.manager.search_book("ვეფხისტყაოსანი")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].author, "შოთა რუსთაველი")

    def test_search_missing_book(self):
        result = self.manager.search_book("არარსებული წიგნი")

        self.assertEqual(len(result), 0)

    def test_delete_book(self):
        self.manager.add_book(self.book)

        deleted = self.manager.delete_book(0)

        self.assertEqual(deleted.title, "ვეფხისტყაოსანი")
        self.assertEqual(len(self.manager.get_all_books()), 0)

    def test_delete_invalid_index(self):
        result = self.manager.delete_book(5)

        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()

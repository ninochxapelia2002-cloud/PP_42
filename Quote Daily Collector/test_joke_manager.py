
import unittest
import tempfile
import os

from joke import Joke
from joke_manager import JokeManager


class TestJokeManager(unittest.TestCase):

    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(
            suffix=".json",
            delete=False
        )
        self.temp_file.close()

        self.manager = JokeManager(self.temp_file.name)

    def tearDown(self):
        if os.path.exists(self.temp_file.name):
            os.remove(self.temp_file.name)

    def test_add_joke(self):
        joke = Joke("Programming", "single", "Test joke")

        self.manager.add_joke(joke)

        self.assertEqual(len(self.manager.get_all_jokes()), 1)

    def test_filter_by_category(self):
        self.manager.add_joke(
            Joke("Programming", "single", "Joke one")
        )
        self.manager.add_joke(
            Joke("Misc", "single", "Joke two")
        )

        result = self.manager.filter_by_category("Programming")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].category, "Programming")

    def test_delete_joke(self):
        joke = Joke("Misc", "single", "Test joke")

        self.manager.add_joke(joke)

        deleted = self.manager.delete_joke(0)

        self.assertIsNotNone(deleted)
        self.assertEqual(len(self.manager.get_all_jokes()), 0)

    def test_delete_invalid_index(self):
        result = self.manager.delete_joke(5)

        self.assertIsNone(result)

    def test_save_and_load_jokes(self):
        joke = Joke("Programming", "single", "Hello world")

        self.manager.add_joke(joke)

        new_manager = JokeManager(self.temp_file.name)

        loaded = new_manager.get_all_jokes()

        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].content, "Hello world")

    def test_empty_list(self):
        self.assertEqual(self.manager.get_all_jokes(), [])


if __name__ == "__main__":
    unittest.main()


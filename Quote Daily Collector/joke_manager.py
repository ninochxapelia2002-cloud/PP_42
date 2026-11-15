
import json
from joke import Joke


class JokeManager:
    def __init__(self, file_path="jokes.json"):
        self.__jokes = []
        self.file_path = file_path
        self.load_jokes()

    def add_joke(self, joke):
        self.__jokes.append(joke)
        self.save_jokes()

    def get_all_jokes(self):
        return self.__jokes.copy()

    def show_jokes(self):
        if not self.__jokes:
            print("შენახული ხუმრობები არ არის.")
            return

        for index, joke in enumerate(self.__jokes, start=1):
            print(f"\nხუმრობა №{index}")
            joke.display_info()

    def filter_by_category(self, category):
        return [
            joke for joke in self.__jokes
            if joke.category.casefold() == category.strip().casefold()
        ]

    def delete_joke(self, index):
        if 0 <= index < len(self.__jokes):
            deleted = self.__jokes.pop(index)
            self.save_jokes()
            return deleted

        return None

    def save_jokes(self):
        data = [
            {
                "category": joke.category,
                "type": joke.joke_type,
                "content": joke.content
            }
            for joke in self.__jokes
        ]

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load_jokes(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, list):
                raise ValueError("არასწორი ფაილის ფორმატი.")

            self.__jokes = [
                Joke(
                    item["category"],
                    item["type"],
                    item["content"]
                )
                for item in data
            ]

        except FileNotFoundError:
            self.__jokes = []

        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            self.__jokes = []

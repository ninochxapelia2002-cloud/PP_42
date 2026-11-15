
import requests
from joke import Joke


class JokeAPI:
    BASE_URL = "https://v2.jokeapi.dev/joke"

    CATEGORIES = [
        "Any",
        "Programming",
        "Misc",
        "Pun",
        "Spooky",
        "Christmas"
    ]

    def get_random_joke(self, category="Any"):
        if category not in self.CATEGORIES:
            raise ValueError("ასეთი კატეგორია არ არსებობს.")

        try:
            response = requests.get(
                f"{self.BASE_URL}/{category}",
                params={"safe-mode": ""},
                timeout=10
            )

            response.raise_for_status()
            data = response.json()

            if data.get("error"):
                return None

            joke_type = data.get("type")

            if joke_type == "single":
                content = data.get("joke", "")

            elif joke_type == "twopart":
                content = (
                    data.get("setup", "")
                    + "\n"
                    + data.get("delivery", "")
                )

            else:
                return None

            if not content.strip():
                return None

            return Joke(
                data.get("category", category),
                joke_type,
                content
            )

        except requests.RequestException:
            print("API-სთან დაკავშირება ვერ მოხერხდა.")
            return None

        except (ValueError, TypeError, AttributeError):
            print("მიღებული მონაცემები არასწორია.")
            return None


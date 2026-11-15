
class Joke:
    def __init__(self, category, joke_type, content):
        if not category.strip():
            raise ValueError("კატეგორია ცარიელი არ უნდა იყოს.")

        if not content.strip():
            raise ValueError("ხუმრობა ცარიელი არ უნდა იყოს.")

        self.__category = category
        self.__type = joke_type
        self.__content = content

    @property
    def category(self):
        return self.__category

    @property
    def joke_type(self):
        return self.__type

    @property
    def content(self):
        return self.__content

    def display_info(self):
        print(f"კატეგორია: {self.category}")
        print(f"ტიპი: {self.joke_type}")
        print(f"ხუმრობა: {self.content}")

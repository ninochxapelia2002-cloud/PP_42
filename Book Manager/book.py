
class Book:
    def __init__(self, title, author, year):
        if not title.strip():
            raise ValueError("სათაური ცარიელი არ უნდა იყოს.")

        if not author.strip():
            raise ValueError("ავტორი ცარიელი არ უნდა იყოს.")

        if not isinstance(year, int) or not 1 <= year <= 2026:
            raise ValueError("გამოცემის წელი არასწორია.")

        self.__title = title.strip()
        self.__author = author.strip()
        self.__year = year

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def year(self):
        return self.__year

    def display_info(self):
        print(f"სათაური: {self.title}")
        print(f"ავტორი: {self.author}")
        print(f"გამოცემის წელი: {self.year}")

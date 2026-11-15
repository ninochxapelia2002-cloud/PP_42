    
class BookManager:
    def __init__(self):
        self.__books = []

    def add_book(self, book):
        self.__books.append(book)

    def get_all_books(self):
        return self.__books.copy()

    def show_books(self):
        if not self.__books:
            print("წიგნების სია ცარიელია.")
            return

        for index, book in enumerate(self.__books, start=1):
            print(f"\nწიგნი №{index}")
            book.display_info()

    def search_book(self, title):
        return [
            book for book in self.__books
            if book.title.casefold() == title.strip().casefold()
        ]

    def delete_book(self, index):
        if 0 <= index < len(self.__books):
            return self.__books.pop(index)

        return None


from book import Book
from book_manager import BookManager


def main():
    manager = BookManager()

    while True:
        print("\n===== BOOK MANAGER =====")
        print("1. ახალი წიგნის დამატება")
        print("2. ყველა წიგნის ნახვა")
        print("3. წიგნის ძებნა")
        print("4. წიგნის წაშლა")
        print("5. გამოსვლა")

        choice = input("აირჩიეთ მოქმედება: ").strip()

        if choice == "1":
            title = input("წიგნის სათაური: ").strip()
            author = input("ავტორი: ").strip()
            year_input = input("გამოცემის წელი: ").strip()

            try:
                year = int(year_input)
                book = Book(title, author, year)
                manager.add_book(book)
                print("წიგნი წარმატებით დაემატა!")

            except ValueError as error:
                print(f"შეცდომა: {error}")

        elif choice == "2":
            manager.show_books()

        elif choice == "3":
            title = input("შეიყვანეთ წიგნის სათაური: ").strip()

            if not title:
                print("სათაური ცარიელი არ უნდა იყოს.")
                continue

            results = manager.search_book(title)

            if results:
                for book in results:
                    book.display_info()
            else:
                print("წიგნი ვერ მოიძებნა.")

        elif choice == "4":
            books = manager.get_all_books()

            if not books:
                print("წიგნების სია ცარიელია.")
                continue

            manager.show_books()

            try:
                index = int(input("წაშალეთ წიგნის ნომერი: "))
                deleted = manager.delete_book(index - 1)

                if deleted:
                    print("წიგნი წარმატებით წაიშალა.")
                else:
                    print("არასწორი ნომერი.")

            except ValueError:
                print("შეიყვანეთ სწორი რიცხვი.")

        elif choice == "5":
            print("პროგრამა დასრულდა.")
            break

        else:
            print("არასწორი არჩევანი.")


if __name__ == "__main__":
    main()

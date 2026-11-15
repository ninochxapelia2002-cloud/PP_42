
from joke_api import JokeAPI
from joke_manager import JokeManager


def main():
    api = JokeAPI()
    manager = JokeManager()

    while True:
        print("\n===== JOKE COLLECTOR =====")
        print("1. შემთხვევითი ხუმრობის მიღება")
        print("2. კატეგორიით ხუმრობის მიღება")
        print("3. შენახული ხუმრობების ნახვა")
        print("4. კატეგორიით გაფილტვრა")
        print("5. ხუმრობის წაშლა")
        print("6. გამოსვლა")

        choice = input("\nაირჩიეთ მოქმედება: ").strip()

        if choice == "1":
            joke = api.get_random_joke()

            if joke:
                joke.display_info()
                save = input("შეინახოთ? (კი/არა): ").strip().lower()

                if save == "კი":
                    manager.add_joke(joke)
                    print("ხუმრობა შენახულია.")

        elif choice == "2":
            print("კატეგორიები:", ", ".join(api.CATEGORIES))
            category = input("შეიყვანეთ კატეგორია: ").strip()

            try:
                joke = api.get_random_joke(category)

                if joke:
                    joke.display_info()
                    manager.add_joke(joke)
                    print("ხუმრობა შენახულია.")

            except ValueError as error:
                print(error)

        elif choice == "3":
            manager.show_jokes()

        elif choice == "4":
            category = input("შეიყვანეთ კატეგორია: ").strip()

            if not category:
                print("კატეგორია ცარიელი არ უნდა იყოს.")
                continue

            results = manager.filter_by_category(category)

            if results:
                for joke in results:
                    joke.display_info()
            else:
                print("ხუმრობები ვერ მოიძებნა.")

        elif choice == "5":
            jokes = manager.get_all_jokes()

            if not jokes:
                print("ხუმრობების სია ცარიელია.")
                continue

            manager.show_jokes()

            try:
                index = int(input("შეიყვანეთ ხუმრობის ნომერი: "))
                deleted = manager.delete_joke(index - 1)

                if deleted:
                    print("ხუმრობა წაიშალა.")
                else:
                    print("არასწორი ნომერი.")

            except ValueError:
                print("შეიყვანეთ სწორი რიცხვი.")

        elif choice == "6":
            print("პროგრამა დასრულდა.")
            break

        else:
            print("არასწორი არჩევანი.")


if __name__ == "__main__":
    main()

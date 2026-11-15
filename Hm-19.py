#Task 1
cart = []
cart.append("ვაშლი")
cart.append("ყველი")
cart.append("პური")
cart.append("რძე")
print("საწყისი კალათა:", cart)
removed_item = cart.pop()
print(f"ამოშლილი პროდუქტი (ბოლო): {removed_item}")
print("კალათის საბოლოო მდგომარეობა:", cart)

#Task 2
visitors = ["gio", "ნინო", "gio", "ანა", "ნიკა", "ანა"]
unique_visitors = set(visitors)
total_unique = len(unique_visitors)
print("უნიკალური ვიზიტორები:", unique_visitors)
print(f"სულ უნიკალური ვიზიტორია: {total_unique}")

#task 3
# 1. ვქმნით ლექსიკონს (dict), სადაც გასაღები არის სახელი, ხოლო მნიშვნელობა - ნომერი
phonebook = {
    "გიორგი": "555123456",
    "ანა": "599789111",
    "ნიკა": "577889900",
    "მარიამი": "511223344"
}
search_name = input("შეიყვანეთ მოსაძებნი სახელი: ")
result = phonebook.get(search_name, "ვერ მოიძებნა")
print(f"ძიების შედეგი ({search_name}): {result}")
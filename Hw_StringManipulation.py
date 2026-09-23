# Task 1
first_name = input("First name: ")
last_name = input("Last name: ")

first_name = first_name.strip().capitalize()
last_name = last_name.strip().capitalize()
print(first_name, last_name)

# Task 2
Text = "My favorite thing is Python"

New_Text = Text.replace("thing", "language")
print(New_Text)

python_index = Text.find("Python")
print(python_index)

Sliced_Text = Text[12:]
print(Sliced_Text)

# Task 3

Name_Customer = input("Enter your name: ")
Name_Company = input("Enter your company name: ")
print(f"Hello {Name_Customer}, your workspace is {Name_Company}.")
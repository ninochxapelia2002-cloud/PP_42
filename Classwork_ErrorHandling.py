#TASK 1
try:
    birth_year = int(input("Please enter your birth year: "))
    age = 2026 - birth_year
    print(age)
except ValueError:
    print("Please enter only digits!")


#TASK 2
try:
    password = input("Please enter a password: ")
    if len(password) < 6:
        raise ValueError("Password is too short!")
except ValueError as e:
    print(e)


    
#Task 1 "Shopping Cart Total & Price Parser"
try:
    price = float(input("Enter the item price: "))
    quantity = int(input("Enter the quantity: "))
    total = price * quantity
except ValueError:
    print("Error: Both price and quantity must be valid numbers!")
else:
    print(f"Total price: ${total:.2f}")

#Task 2 "User Age Validator"

try:
    age = int(input("Enter your age: "))
    
    if age < 0:
        raise ValueError("Age cannot be negative!")
    elif age < 18:
        raise ValueError("User must be at least 18 years old to register.")

except ValueError as e:
    print(e)

finally:
    print("Registration process completed.")

#Task 3 "Safe List Index Accessor"

fruits = ["apple", "banana", "cherry", "orange"]

try:
    index = int(input("Enter an index number: "))
    print(f"Selected fruit: {fruits[index]}")
except ValueError:
    print("Invalid input! Please enter a whole number.")
except IndexError:
    print(f"Index out of bounds! Choose an index between 0 and {len(fruits)-1}.")
else:
    print("Successfully retrieved item!")
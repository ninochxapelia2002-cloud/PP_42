#Task 1 -> Secret PIN Code
correct_pin = "1234"
attempts = 3

while attempts > 0:
    user_pin = input("Enter the Correct PIN: ")
    
    if user_pin == correct_pin:
        print("Access granted!")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Incorrect PIN. Remaining attempts: {attempts}")
        else:
            print("Card blocked!")

#Task 2 -> Sum of Even Numbers

n = int(input("Enter a positive integer n: "))

total_sum = 0

for i in range(2, n + 1, 2):
    total_sum += i

print(f"The sum of even numbers from 1 to {n} is: {total_sum}")

#Task 3 -> Text Filter — Skip Digits

# Task 3
text = input("Enter text: ")

result = ""

for char in text:
    if char.isdigit():
        continue
    result += char

print(result)
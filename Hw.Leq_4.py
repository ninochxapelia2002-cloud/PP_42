# Task 1: Smart Movie Theater Ticket Pricing
Age = input("Enter your age: ")

if Age < 0 : 
    print("Invalid age entered.")
elif Age < 5 :
    print("Your ticket price is $0.")
elif Age <= 12 :
    print("Your ticket price is $8.")
elif Age <= 64 :
    print("Your ticket price is $15.")
else:
    print("Your ticket price is $10.")

#Task 2: E-Commerce Discount & Free Shipping
cart_total = 60.0  
is_vip = False     
is_guest = False   
promo_code = "SAVE10"  


if cart_total >= 50 or is_vip:
    print("You get Free Shipping!")
else:
    print("You pay for shipping.")

if promo_code and not is_guest:
    final_price = cart_total * 0.9
    print(f"The 10% discount was applied. Final total price: ${final_price}")
else:
    final_price = cart_total
    print(f"No discount applied. Final total price: ${final_price}")

#Task 3: Smart ATM Cash Withdrawal

correct_pin = 1234
balance = 500.0
requested_amount = 100.0
entered_pin = int(input("Enter your PIN: "))
if entered_pin == correct_pin:
    if requested_amount <= balance:
        balance -= requested_amount
        print(f"Withdrawal successful! Remaining balance: ${balance}")
    else:
        print("Amount of your balance isn't enough.")
else:
    print("Incorrect PIN. Access Denied.")
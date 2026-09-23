from math import sqrt
## 1
Person_Name = "Nino Chkhapelia"
Person_Age = 23
Is_Employed = True
love_number = sqrt(2)

print(type(Person_Name))
print(type(Person_Age))
print(type(Is_Employed))
print(type(love_number))

## 2
Birth_year = int(input("Enter your birth year: "))

Age = 2026 - Birth_year

print("Your approximate age is:", Age)


## 3
Number = int(input("Enter a number: "))

if Number > 0:
    print("Positive")
elif Number < 0:
    print("Negative")
else:
    print("Zero")

if Number % 2 == 0:
    print("Even")
else:
    print("Odd")
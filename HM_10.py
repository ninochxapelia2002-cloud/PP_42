#task 1
def sum_of_digits(n):
    if n < 10:
        return n

    return (n % 10) + sum_of_digits(n // 10)


print(sum_of_digits(1234)) 

#task 2
scores = [45, 82, 67, 38, 90, 55, 72]

passing_scores = list(filter(lambda x: x >= 50, scores))

final_scores = list(map(lambda x: min(100, x + 5), passing_scores))

print("Filtered scores:", passing_scores)
print("Final scores with bonus:", final_scores)

#task 3

names = ["Laptop", "Phone", "Headphones", "Monitor"]
prices = [1200, 800, 150, 300]
ratings = [4.8, 4.5, 4.2, 4.9]

products = list(zip(names, prices, ratings))

by_price_desc = sorted(products, key=lambda item: item[1], reverse=True)

by_rating_asc = sorted(products, key=lambda item: item[2])

print("ფასის კლების მიხედვით (ძვირიდან იაფისკენ):")
print(by_price_desc)

print("\nრეიტინგის ზრდის მიხედვით (დაბლიდან მაღლისკენ):")
print(by_rating_asc)
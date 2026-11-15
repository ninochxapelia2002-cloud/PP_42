#Task 1: Student Score Manager 
scores = []

scores.append(45)
scores.append(88)
scores.append(92)
scores.append(60)
scores.append(75)

scores.remove(45)

average_score = sum(scores) / len(scores)
highest_score = max(scores)
lowest_score = min(scores)
print("Average:", average_score)
print("Highest:", highest_score)
print("Lowest:", lowest_score)

scores.sort()
print("Sorted scores:", scores)

passed_scores = [score for score in scores if score >= 60]
print("Passed scores:", passed_scores)


#Task 2: Store Inventory Update

inventory = ["apple", "banana", "orange", "apple", "kiwi", "apple"]
new_items = ["mango", "grape"]

apple_count = inventory.count("apple")
print("Apple count:", apple_count)

orange_index = inventory.index("orange")
print("Orange index:", orange_index)

inventory.extend(new_items)
print("Extended inventory:", inventory)


print("Reversed inventory:", inventory[::-1])

#Task 3: Travel Itinerary

locations = [
    ("Tbilisi", 41.71, 44.82),
    ("Batumi", 41.64, 41.63),
    ("Kutaisi", 42.26, 42.71)
]

for city, Latitude, Longitude in locations:
    print(f"City: {city}, Latitude: {Latitude}, Longitude: {Longitude}")

city_names = [city for city, Latitude, Longitude in locations]
print(city_names)
#Task 1: “Set Operations” 

frontend_skills = {"HTML", "CSS", "JavaScript", "React"}
backend_skills = {"Python", "JavaScript", "SQL", "React"}

print("Union:", frontend_skills | backend_skills)
print("Intersection:", frontend_skills & backend_skills)

print("Frontend-only difference:", frontend_skills - backend_skills)


print("Symmetric difference:", frontend_skills ^ backend_skills)

#Task 2: “Nested Dictionary Extraction & Update” 

student = {
    "name": "Ana",
    "age": 20,
    "contacts": {
        "email": "ana@example.com",
        "phone": "599123456"
    },
    "courses": {
        "python": {"score": 95, "passed": True},
        "web": {"score": 58, "passed": False}
    }
}
print("Email:", student["contacts"]["email"])

print("Python score:", student["courses"]["python"]["score"])

student["courses"]["web"]["passed"] = True
student["courses"]["web"]["score"] = 65

student["contacts"].pop("phone")

print("Updated student:", student)

#Task 3: “Word Frequency Counter” 

words = ["apple", "banana", "apple", "cherry", "banana", "apple", "orange"]

word_counts = {}

for w in words:
    word_counts[w] = word_counts.get(w, 0) + 1

print("Word frequencies:", word_counts)

print("\nWords appearing more than once:")
for word, count in word_counts.items():
    if count > 1:
        print(f"{word}: {count}")


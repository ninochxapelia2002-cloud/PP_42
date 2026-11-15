##Task 1 — Infinite Even Numbers
def even_numbers():
    num = 0
    while True:
        yield num
        num += 2  

count = 0
for n in even_numbers():
    if count >= 10:
        break
    print(n)
    count += 1

##Task 2 — Word Length Filter 

words = ["python", "generator", "yield", "code", "ai", "developer"]

filtered_words = (word.upper() for word in words if len(word) > 4)

for w in filtered_words:
    print(w)

##Task 3 — Greeter Bot 

def greeter_bot():
    name = yield "Enter your name"

    while True:

        name = yield f"Hello, {name}!"

bot = greeter_bot()

print(next(bot)) 

print(bot.send("გიორგი"))  
print(bot.send("ნინო")) 
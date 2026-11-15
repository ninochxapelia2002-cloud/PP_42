import time
import asyncio
import aiohttp
import requests

# Task 1: სინქრონული (requests) vs ასინქრონული (aiohttp) 10 ჩანაწერისთვის

print("=== Task 1: სინქრონული და ასინქრონული მიდგომის შედარება ===")

URLS = [f"https://jsonplaceholder.typicode.com/todos/{i}" for i in range(1, 11)]


start_time = time.time()
sync_results = []
for url in URLS:
    response = requests.get(url)
    sync_results.append(response.json())
sync_time = time.time() - start_time
print(f"სინქრონულმა ვერსიამ იმუშავა: {sync_time:.4f} წამში")

async def fetch_todo(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main_task1():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_todo(session, url) for url in URLS]
        return await asyncio.gather(*tasks)

start_time = time.time()
async_results = asyncio.run(main_task1())
async_time = time.time() - start_time
print(f"ასინქრონულმა ვერსიამ იმუშავა: {async_time:.4f} წამში")


difference = sync_time - async_time
print(f"ასინქრონულმა ვერსიამ {difference:.4f} წამით უფრო სწრაფად იმუშავა!\n")

# Task 2: ასინქრონული მოთხოვნა და ფილტრაცია (userId == 1)

print("=== Task 2: პოსტების წამოღება და ფილტრაცია userId-ის მიხედვით ===")
POSTS_URL = "https://jsonplaceholder.typicode.com/posts"

async def fetch_posts():
    async with aiohttp.ClientSession() as session:
        async with session.get(POSTS_URL) as response:
            return await response.json()

async def main_task2():
    posts = await fetch_posts()
    

    filtered_posts = [p for p in posts if p.get("userId") == 1]
    
    print("მხოლოდ userId=1 მქონე პოსტების სათაურები (title):")
    for post in filtered_posts:
        print(f"- {post.get('title')}")

asyncio.run(main_task2())
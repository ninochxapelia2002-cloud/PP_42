import time
import requests
from multiprocessing import Process
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

# დავალება 1: CPU-Bound დატვირთვა და Multiprocessing
def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# დავალება 2: I/O-Bound & Threads (100 Thread)

API_URL = "https://jsonplaceholder.typicode.com/posts/1"

def fetch_data():
    try:
        response = requests.get(API_URL, timeout=5)
        response.json()
    except Exception:
        pass

# დავალება 3: ThreadPoolExecutor

def fetch_with_id(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    try:
        response = requests.get(url, timeout=5)
        return response.json()
    except Exception:
        return None


if __name__ == '__main__':
    # --- დავალება 1-ის გაშვება ---
    print("=== დავალება 1: CPU-Bound (ფაქტორიალი) ===")
    big_number = 70000

    # 1. Single-process დროის გაზომვა
    start_time = time.time()
    calculate_factorial(big_number)
    calculate_factorial(big_number)
    single_process_time = time.time() - start_time
    print(f"Single-process დრო: {single_process_time:.4f} წამი")

    # 2. Multiprocessing დროის გაზომვა
    start_time = time.time()
    p1 = Process(target=calculate_factorial, args=(big_number,))
    p2 = Process(target=calculate_factorial, args=(big_number,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    multiprocessing_time = time.time() - start_time
    print(f"Multiprocessing დრო: {multiprocessing_time:.4f} წამი\n")


    # --- დავალება 2-ის გაშვება ---
    print("=== დავალება 2: I/O-Bound (100 Thread) ===")
    start_time = time.time()
    threads = []

    for _ in range(100):
        t = Thread(target=fetch_data)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    threads_time = time.time() - start_time
    print(f"100 ცალკეული Thread-ის შესრულების დრო: {threads_time:.4f} წამი\n")


    # --- დავალება 3-ის გაშვება ---
    print("=== დავალება 3: ThreadPoolExecutor ===")
    start_time = time.time()

    post_ids = list(range(1, 101))
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(fetch_with_id, post_ids))

    pool_time = time.time() - start_time
    print(f"ThreadPoolExecutor-ის შესრულების დრო: {pool_time:.4f} წამი")
    print(f"წამოღებული პოსტების რაოდენობა: {len([r for r in results if r])}")
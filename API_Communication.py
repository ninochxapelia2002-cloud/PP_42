import requests

BASE_URL = "https://crudcrud.com/api/your_unique_endpoint_here/products"
product_id = None

# TASK 1: პროდუქტის დამატება (POST)

print("=== TASK 1: პროდუქტის დამატება ===")
product_data = {
    "name": "Laptop",
    "price": 2500,
    "in_stock": True
}

try:
    response = requests.post(BASE_URL, json=product_data, timeout=5)
    response.raise_for_status()
    created_product = response.json()
    print("პროდუქტი წარმატებით დაემატა:", created_product)
    
    # ვიმახსოვრებთ ავტომატურად გენერირებულ _id-ს
    product_id = created_product.get("_id")
    print(f"მიღებული _id: {product_id}\n")
except requests.exceptions.RequestException as e:
    print(f"შეცდომა Task 1-ში: {e}\n")



# TASK 2: ყველა პროდუქტის სიის წამოღება (GET)

print("=== TASK 2: ყველა პროდუქტის სია ===")
try:
    response = requests.get(BASE_URL, timeout=5)
    response.raise_for_status()
    products = response.json()
    
    print("პროდუქტების სია:")
    for p in products:
        print(f"სახელი: {p.get('name')} | ფასი: {p.get('price')} | ID: {p.get('_id')}")
    print()
except requests.exceptions.RequestException as e:
    print(f"შეცდომა Task 2-ში: {e}\n")



# TASK 3: ერთი პროდუქტის წამოღება _id-ით (GET)

print("=== TASK 3: ერთი პროდუქტის წამოღება ID-ით ===")
if product_id:
    single_url = f"{BASE_URL}/{product_id}"
    try:
        response = requests.get(single_url, timeout=5)
        response.raise_for_status()
        print("ნაპოვნი პროდუქტი:", response.json(), "\n")
    except requests.exceptions.RequestException as e:
        print(f"შეცდომა Task 3-ში: {e}\n")
else:
    print("ID ვერ მოიძებნა, რადგან Task 1 ვერ შესრულდა.\n")



# TASK 4: პროდუქტის განახლება (PUT)

print("=== TASK 4: პროდუქტის განახლება ===")
if product_id:
    single_url = f"{BASE_URL}/{product_id}"
    updated_data = {
        "name": "Gaming Laptop",
        "price": 3200,
        "in_stock": True
    }
    
    try:
        response = requests.put(single_url, json=updated_data, timeout=5)
        response.raise_for_status()
        print("პროდუქტი განახლდა. სტატუს კოდი:", response.status_code)
        
        # გადამოწმება განახლების შემდეგ
        check_response = requests.get(single_url, timeout=5)
        check_response.raise_for_status()
        print("განახლებული მონაცემები:", check_response.json(), "\n")
    except requests.exceptions.RequestException as e:
        print(f"შეცდომა Task 4-ში: {e}\n")
else:
    print("ID ვერ მოიძებნა განახლებისთვის.\n")



# TASK 5: პროდუქტის წაშლა (DELETE)

print("=== TASK 5: პროდუქტის წაშლა ===")
if product_id:
    single_url = f"{BASE_URL}/{product_id}"
    try:
        response = requests.delete(single_url, timeout=5)
        response.raise_for_status()
        print(f"პროდუქტი ID-ით {product_id} წარმატებით წაიშალა სერვერიდან!")
    except requests.exceptions.RequestException as e:
        print(f"შეცდომა Task 5-ში: {e}")
else:
    print("ID ვერ მოიძებნა წაშლისთვის.")
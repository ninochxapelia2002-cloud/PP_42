from dataclasses import dataclass, asdict
import json

#1
@dataclass
class Product:
    name: str
    price: float
    in_stock: bool
product1 = Product(name="ლეპტოპი", price=2500.0, in_stock=True)
product2 = Product(name="მაუსი", price=75.5, in_stock=True)
product3 = Product(name="სათვალე", price=120.0, in_stock=False)
print("--- დავალება 1: შექმნილი ობიექტები ---")
print(product1)
print(product2)
print(product3)

#2
products_list = [asdict(product1), asdict(product2), asdict(product3)]
json_string = json.dumps(products_list, indent=4, ensure_ascii=False)

print("\n დავალება 2: JSON სერიალიზაცია ")
print(json_string)

# დავალება 3: JSON დესერიალიზაცია
raw_json_data = '{"name": "Laptop", "price": 2500, "in_stock": true}'
parsed_dict = json.loads(raw_json_data)
restored_product = Product(**parsed_dict)

print("\n დავალება 3: JSON დესერიალიზაცია")
print(f"ტიპი: {type(restored_product)}")
print(f"ატრიბუტები: სახელი - {restored_product.name}, ფასი - {restored_product.price}, მარაგშია - {restored_product.in_stock}")
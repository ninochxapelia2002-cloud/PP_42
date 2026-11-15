## 1
class MovieTicket:
    cinema_name = "Rustaveli Cinema"
    total_tickets_sold = 0

    def __init__(self, movie_title, seat_number, price):
        self.movie_title = movie_title
        self.seat_number = seat_number
        self.price = price
        MovieTicket.total_tickets_sold += 1

ticket1 = MovieTicket("Avatar 2", 12, 25.0)
ticket2 = MovieTicket("Oppenheimer", 5, 20.0)
ticket3 = MovieTicket("Interstellar", 18, 22.5)

print(f"ბილეთი 1: კინოთეატრი - {ticket1.cinema_name}, ფილმი - {ticket1.movie_title}, ადგილი - {ticket1.seat_number}, ფასი - {ticket1.price}₾")
print(f"ბილეთი 2: კინოთეატრი - {ticket2.cinema_name}, ფილმი - {ticket2.movie_title}, ადგილი - {ticket2.seat_number}, ფასი - {ticket2.price}₾")
print(f"ბილეთი 3: კინოთეატრი - {ticket3.cinema_name}, ფილმი - {ticket3.movie_title}, ადგილი - {ticket3.seat_number}, ფასი - {ticket3.price}₾")

print(f"\nსულ გაყიდული ბილეთების რაოდენობა: {MovieTicket.total_tickets_sold}")

## 2
class User:
    status = "Active"

    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age

    def get_info(self):
        print(f"მომხმარებელი: {self.username}, ელ-ფოსტა: {self.email}, ასაკი: {self.age}, სტატუსი: {self.status}")

user1 = User("gio123", "gio@gmail.com", 22)
user2 = User("salome_n", "salome@gmail.com", 25)

user1.get_info()
user2.get_info()

print(f"User 1 სტატუსი: {user1.status}")
print(f"User 2 სტატუსი: {user2.status}")

##  3

class Product:
    shop_name = "MegaShop"

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            print(f"გაიყიდა {quantity} ცალი {self.name}, დარჩა: {self.stock}")
        else:
            print(f"მარაგში არ არის საკმარისი {self.name} (ხელმისაწვდომია: {self.stock})")

product1 = Product("Laptop", 1500.0, 10)

product1.sell(2)
product1.sell(3)
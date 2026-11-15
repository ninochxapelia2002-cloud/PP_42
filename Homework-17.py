# task 1
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary 
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, value):
        if value < 0:
            print("ხელფასი უარყოფითი ვერ იქნება!")
        else:
            self.__salary = value
    @salary.deleter
    def salary(self):
        print("ხელფასის ატრიბუტი წაიშალა")
        del self.__salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    def get_info(self):
        print(f"სახელი: {self.name}, განყოფილება: {self.department}, ხელფასი: {self.salary}")

mgr = Manager("გიორგი", 3500, "IT")
try:
    print(mgr.__salary)
except AttributeError:
    print("შეცდომა:salary არის private ატრიბუტი და პირდაპირ ვერ დავუკავშირდებით!")
mgr.get_info()
mgr.salary = 4000  
mgr.get_info()

#task 2
class Payment:
    def process_payment(self, amount):
        print(f"მუშავდება გადახდა. თანხა: {amount} ლარი")
class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"საბანკო ბარათით გადახდილია: {amount} ლარი")
class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"PayPal-ით გადახდილია: {amount} ლარი")
def make_payment(payment_object, amount):
    payment_object.process_payment(amount)
base_payment = Payment()
cc_payment = CreditCardPayment()
paypal_payment = PayPalPayment()

print("ტესტირება")
base_payment.process_payment(100)
cc_payment.process_payment(250)
paypal_payment.process_payment(150)

#task 3
class SmartDevice:
    def __init__(self, brand):
        self.brand = brand
        self.__is_on = False
    def turn_on(self):
        self.__is_on = True
        print(f"{self.brand} მოწყობილობა ჩაირთო.")
    def turn_off(self):
        self.__is_on = False
        print(f"{self.brand} მოწყობილობა ითიშება.")
    @property
    def is_on(self):
        return self.__is_on

class SmartLight(SmartDevice):
    def __init__(self, brand, brightness=50):
        super().__init__(brand)
        self.brightness = brightness  
    def turn_on(self):
        super().turn_on()
        print(f"ბრენდი: {self.brand}, სიკაშკაშე: {self.brightness}%")
lamp = SmartLight("Xiaomi", 80)
print(f"სტატუსი ჩართვამდე: {lamp.is_on}")
lamp.turn_on()
print(f"სტატუსი ჩართვის შემდეგ: {lamp.is_on}")
lamp.turn_off()
print(f"სტატუსი გამორთვის შემდეგ: {lamp.is_on}")
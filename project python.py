# user data 
import random
name = str (input('enter ur name' ))
pasword = str(input('enter ur paswoord:'))
verfication_code= random.random()
print(f"Verification code is: {verfication_code}")
entered_code= input ('enter the verification code: ')
if entered_code == verfication_code:
    print('wellcome')
else:
    print ('invalid verification code')
exit()
# display data 
from prettytable import PrettyTable 
t1 = PrettyTable (['name','price','quantity']) 
t1.add_row(['nootbook','50','500'])
t1.add_row(['pen','10','1000'])
t1.add_row(['pencile','5','1500'])
t1.add_row(['eraser','3','800'])
t1.add_row(['rular','20','300'])
print(t1)
from prettytable import PrettyTable 
t2 = PrettyTable (['name','price','quantity']) 
t2.add_row(['wter','80','1200'])
t2.add_row(['soda','130','1200'])
t2.add_row(['chips','75','1200'])
t2.add_row(['bread','45','1200'])
t2.add_row(['ruleggsar','65','1200'])
print(t2)
class Product:
    def _init_(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def _str_(self):
        return f"{self.name} - Price: ${self.price:.2f}, Stock: {self.stock}"


class MainStore:
    def _init_(self):
        self.products = [
            Product("Water", 1.00, 1000),
            Product("Soda", 1.50, 500),
            Product("Bread", 2.00, 300)
        ]

    def display_products(self):
        print("\nMain Store Products:")
        for product in self.products:
            print(product)

    def calculate_discount(self, quantity):
        discount = min((quantity // 250) * 5, 25)  # Max discount of 25%
        return discount

    def purchase(self, product_name, quantity):
        for product in self.products:
            if product.name.lower() == product_name.lower():
                if product.stock >= quantity:
                    product.stock -= quantity
                    discount = self.calculate_discount(quantity)
                    total_price = quantity * product.price * (1 - discount / 100)
                    return total_price, discount
                else:
                    print("Not enough stock!")
                    return None, None
        print("Product not found!")
        return None, None


class StationaryStore:
    def _init_(self):
        self.products = [
            Product("Pen", 0.50, 200),
            Product("Notebook", 2.50, 150),
            Product("Eraser", 0.25, 100)
        ]

    def display_products(self):
        print("\nStationary Store Products:")
        for product in self.products:
            print(product)

    def calculate_loyalty_discount(self, quantity):
        return (quantity // 50) * 2  # 2% for every 50 units

    def purchase(self, product_name, quantity):
        for product in self.products:
            if product.name.lower() == product_name.lower():
                if product.stock >= quantity:
                    product.stock -= quantity
                    discount = self.calculate_loyalty_discount(quantity)
                    total_price = quantity * product.price * (1 - discount / 100)
                    return total_price, discount
                else:
                    print("Not enough stock!")
                    return None, None
        print("Product not found!")
        return None, None


def main():
    main_store = MainStore()
    stationary_store = StationaryStore()

    while True:
        print("\nWelcome to the Store System!")
        print("1. Main Store")
        print("2. Stationary Store")
        print("3. Exit")
        choice = input("Select a store: ")

        if choice == '1':
            main_store.display_products()
            product_name = input("Enter product name to purchase: ")
            quantity = int(input("Enter quantity: "))
            total_price, discount = main_store.purchase(product_name, quantity)
            if total_price is not None:
                print(f"Total price after {discount}% discount: ${total_price:.2f}")

        elif choice == '2':
            stationary_store.display_products()
            product_name = input("Enter product name to purchase: ")
            quantity = int(input("Enter quantity: "))
            total_price, discount = stationary_store.purchase(product_name, quantity)
            if total_price is not None:
                print(f"Total price after {discount}% loyalty discount: ${total_price:.2f}")

        elif choice == '3':
            print("Thank you for visiting!")
            break

        else:
            print("Invalid choice! Please try again.")


if _name_ == "_main_":
    main()


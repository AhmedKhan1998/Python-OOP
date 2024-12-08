class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return f"User(username={self.username}, email={self.email})"


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"


class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if isinstance(product, Product):
            self.products.append(product)
            print(f"Product {product.name} added to the shop.")
        else:
            print("Invalid product.")

    def display_products(self):
        if not self.products:
            print("No products available in the shop.")
        else:
            print("Products available in the shop:")
            for product in self.products:
                print(f"- {product.name}: ${product.price} (Quantity: {product.quantity})")

    def purchase_product(self, user, product_name, quantity):
        for product in self.products:
            if product.name == product_name:
                if product.quantity >= quantity:
                    product.quantity -= quantity
                    total_price = product.price * quantity
                    print(
                        f"User {user.username} purchased {quantity} x {product.name} for ${total_price}."
                    )
                    if product.quantity == 0:
                        self.products.remove(product)
                        print(f"{product.name} is now out of stock and removed from the shop.")
                    return
                else:
                    print(f"Insufficient stock for {product.name}. Available: {product.quantity}")
                    return
        print(f"Product {product_name} not found in the shop.")


# Example usage
user1 = User("john_doe", "john.doe@example.com")
user2 = User("jane_smith", "jane.smith@example.com")

prod1 = Product("Laptop", 1200, 5)
prod2 = Product("Headphones", 150, 10)
prod3 = Product("Mouse", 25, 20)

shop = Shop()
shop.add_product(prod1)
shop.add_product(prod2)
shop.add_product(prod3)

shop.display_products()

shop.purchase_product(user1, "Laptop", 2)
shop.purchase_product(user2, "Headphones", 1)
shop.purchase_product(user1, "Mouse", 25)

shop.display_products()

class Cart:
    def __init__(self, customer):
        self.checkout_product = []
        self.customer = customer

    def add_product(self, products):
        while True:
            choice = input("What product would you like to add dear customer[enter (d)one]: ").strip()
            if any(choice.lower() == product.product_name.lower() for product in products):
                product = list(filter(lambda product: product.product_name.lower() == choice.lower(), products))[0]
                if product.quantity > 0:
                    self.checkout_product.append(product)
                    product.quantity -= 1
                    print(f"product {product.product_name} add to your cart")
                else:
                    print("\nSorry that product have been sold out!\n")
            elif choice == "d":
                self.customer.add_carinfo()
                break
            else:
                print("Try again, invalid name on product!")

    def price(self):
        return sum(product.sell_price for product in self.checkout_product)

    def ls(self):
        print("Products in cart: ")
        for i, product in enumerate(self.checkout_product):
            print("+"+("-"*25)+"+")
            print("|", f"{product.product_name}".ljust(23), "|")
            print("|", f"Price {product.sell_price} sek".ljust(23), "|")
            print("|", f"{product.description}".ljust(23), "|")
            print("+"+("-"*25)+"+")
        print("\nTotal Price: ", self.price(),"sek\n")


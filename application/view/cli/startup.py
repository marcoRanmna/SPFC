from application.dll.models import Product, Supplier
from application.bll.supplier_controller import get_all_suppliers
from application.bll.product_controller import get_all_products
from application.view.cli.newcustomer import Customer
from application.view.cli.producthandler import ProductsHandler
from application.view.cli.cart import Cart
from application.view.cli.persons import Person
from application.view.cli.company import Company
from application.view.cli.packages import Package
from application.dll.db.db import session
from datetime import datetime

def introduction():
    message = ['New Customer', 'Old customer', 'ourCompany Employee']
    func = [new_customer, old_customer, ourCompany]
    options = dict(zip(message,func))

    print("\n======= Welcome Evil Corp =======\n")
    for index in range(len(message)):
        print(f"({index+1})",message[index])

    choice = input("\nEnter: ")

    if choice.isdigit and -1 < int(choice) < len(message):
        options[message[int(choice)-1]]()


def new_customer():
    print("\n======= Nice to meet you new customer =======\n")
    print("Are you a private person or a Corporation overload like us?")
    print("","(1) Private Person\n", "(2) Company")
    priv_or_corp = "0"
    while priv_or_corp != "1" and priv_or_corp != "2":
        priv_or_corp = input("Select: ").strip()
        if priv_or_corp != "1" and priv_or_corp != "2":
            print("Enter the number in ( x )")

    if priv_or_corp == "2":
        newcompany = Company.coperate_hello()
    else:
        newcompany = None
    customer = Customer.carintroduction(priv_or_corp)
    avliable_product = ProductsHandler(customer)
    shop(customer, avliable_product, newcompany)


def old_customer():
    print("Previous customer")

def ourCompany():
    pass

def shop(customer, avliable_product, company):
    cart = Cart(customer)

    def user_search():
        print("[Press enter to see all relevant products for you]")
        print("[use * as a wildcard to indicate unknown characters]")
        search = input("Search: ")
        avliable_product.refresh(search) 
        avliable_product.ls()

    print("\n======= Evil Corp Shop =======\n")
    print("Hi, dear valued customer what product could I interest you in?")
    user_search()
    while True:
        print("Would you like:\n","(1) add product to cart\n", 
                "(2) retry search\n","(3) Proceed to checkout line\n",
                "(4) Try another car\n", "(e) Exit")
        action = input("Action: ").strip()

        if action == "1":
            cart.add_product(avliable_product.customer_products)
        elif action == "2":
            user_search()
        elif action == "3":
            customer.add_carinfo()
            checkout(cart, customer, company) 
            break
        elif action == "4":
            customer = Customer.carintroduction()
            avliable_product = ProductsHandler(customer)
            user_search()
        elif action == "e":
            break
        else:
            print("Wrong input, use the character indicated in parentheses (x)")

def checkout(cart, customer, company):
    print("\n======= Checkout Line =======\n")
    cart.ls()
    print("To have your product(s) delivered to you dear customer.")
    print("Evil Corp must have certain information about you to validate you :)")
    name = input("Your first and last name: ").strip().split(" ")
    phone = input("Your phone number: ").strip()
    email = input("Your email address: ").strip()
    color = input("Color of your car: ").strip()
    reg_number = input("Your car registration number: ").strip()

    if customer.priv_or_corp == 2:
        user = Person(name[0], name[1], phone, email)
        company.contact_persons.append(user)
    else: 
        user = Person(name[0], name[1], phone, email)
    customer.completed(reg_number, color)

    print("\nAlmost done!\nNow need the address to deliver your product to.")
    country = input("Country to deliver to: ")
    state = input("State: ")
    city = input("City: ")
    zipcode = input("zipcode: ")
    address = input("Address: ")
    user.add_address(country, state, city, zipcode, address)

    print("This is the supplier/suppliers of your product")
    supplier_name = []
    for product in cart.checkout_product:
        products = get_all_suppliers((Product).filter_by(product_name=product).first())
        id = products['idProducts']
        suppliers = session.query(Supplier).filter_by(Products_idProducts=id).first()
        for supplier in suppliers:
            print(supplier['company_name'])
            supplier_name.append(supplier['company_name'])
    running = True
    while running:
        choice = input('Which do you choose? ')
        if choice in supplier_name:
            print(f'Thanks for using {choice}')
            running = False
        else:
            print(f'Your {choice} is misspelled or it does not exist, try again')


    date_format = "%Y-%m-%d"
    requireddate_str = input("Do you have a required date[format YYYY-mm-dd]: ").strip()
    requireddate = requireddate_str.split("-")
    valid_date = len(requireddate) == 3 and all(d.isdigit() for d in requireddate) and datetime.today() < datetime.strptime(requireddate_str, date_format)
    comment = input("Do you have any comments: ")
    if valid_date:
        customer.packages.append(Package(cart.checkout_product,requireddate=datetime.strptime(requireddate_str, date_format), comments=comment))
    else:
        customer.packages.append(Package(cart.checkout_product,comments=comment))

    session_commit(customer, user, company)

def session_commit(customer, user, company):
    if customer.priv_or_corp == 2:
        company.commit()
        customer.commit(user.address[0], corp=company)
    else:
        user.commit()
        customer.commit(user.address[0], private=user)


if __name__ == '__main__':
    introduction()


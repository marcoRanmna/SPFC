def menu():
    print("Welcome to the Spare Parts Shop")
    print()
    print("1. Orders")
    print("2. Products")
    print("3. Manufacturers")
    print("4. Suppliers")
    print("5. Customers")
    print()
    print("9. Quit")
    while True:
        pick = input("> ")
        if pick in "123459":
            break
        print("Valid options are 1, 2, 3, or 9")
    return pick

from application.view.cli.menu import menu
from application.view.cli.orders import view_orders, add_order, delete_record


def main():
    while True:
        menu_pick = menu()
        if menu_pick == "1":
            print("1. View Orders")
            print("2. Add Order")
            print("3. Delete Orders")
            pick = input('> ')
            if pick == 1:
                view_orders()
            if pick == 2:
                add_order()
            if pick == 3:
                delete_record()
        if menu_pick == "2":
            print("1. View Products")
            print("2. Add Product")
            print("3. Delete Product")
            pick = input('> ')
            if pick == 1:
                pass
            if pick == 2:
                pass
            if pick == 3:
                pass
        if menu_pick == "3":
            print("1. View Manufacturers")
            print("2. Add Manufacturer")
            print("3. Delete Manufacturers")
            pick = input('> ')
            if pick == 1:
                pass
            if pick == 2:
                pass
            if pick == 3:
                pass
        if menu_pick == "4":
            print("1. View Suppliers")
            print("2. Add Supplier")
            print("3. Delete Suppliers")
            pick = input('> ')
            if pick == 1:
                pass
            if pick == 2:
                pass
            if pick == 3:
                pass
        if menu_pick == "5":
            print("1. View Customers")
            print("2. Add Customer")
            print("3. Delete Customers")
            pick = input('> ')
            if pick == 1:
                pass
            if pick == 2:
                pass
            if pick == 3:
                pass
        if menu_pick == "9":
            break
        break


if __name__ == '__main__':
    main()
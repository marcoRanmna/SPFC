from application.view.cli.menu import menu
from application.view.cli.orders import view_orders, add_order, delete_record

def main():
    menu_choice = { 1:'Orders', 
                    2:'Products', 
                    3:'Manufacturers', 
                    4:'Suppliers', 
                    5:'Customers', 
                    9:'Quit'}

    menu_operations = {1:'View', 2:'Add', 3: 'Delete'}
    menu_func = {"Orders": (view_orders, add_order, delete_record), 
                "Products": (None, None, None),
                "Manufacturers": (None, None, None),
                "Suppliers": (None, None, None),
                "Customers": (None, None, None),
                "Quit": ("Quit")}

    while True:
        menu_pick = menu(menu_choice)

        for ops in menu_operations:
            print(f"{ops}.", menu_operations[ops], menu_choice[menu_pick])

        pick = input('> ')
        if pick.isdigit() and 0 < int(pick) < len(menu_func[menu_choice[menu_pick]]):
            run = menu_func[menu_choice[menu_pick]][int(pick)-1]
            if not run is None:
                run()
            elif run == 'Quit':
                return 0
        break

if __name__ == '__main__':
    main()

def menu(menu_user_choice: dict):
    print("="*5+"Welcome to the Spare Parts Shop"+"="*5+"\n")
    print("What would you like to do?")
    for choice in menu_user_choice:
        print(f"{choice}. {menu_user_choice[choice]}")

    while True:
        pick = input("> ")
        if pick.isdigit() and int(pick) in menu_user_choice:
            return int(pick)
        print("Valid options are {}\n".format(", ".join([str(key) for key in menu_user_choice])))

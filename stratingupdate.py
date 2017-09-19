def start_chat(name, age, rating):
show_menu = True
    menu_choices = "What do you want to dp ? \n 1. Add Status. \n 2. Close Application"



while show_menu:
    result = int(raw_input(menu_choices))

    # validating users input
    if (result == 1):
        # action 1
        pass
    elif (result == 2):
        show_menu = False
    else:
        print "wrong choice try again."
from textwrap import dedent

def welcome():
    print(dedent("""
    **  Welcome to Snakes Cafe!  **
    **  Please see our menu below.  **
    **
    **  To quit at any time, type "quit"  **
    ****************************************
    """))

welcome()

def appetizers():
    print(dedent("""
    Appetizers
    -------
    Wings
    Cookies
    Spring Rolls
    """))

def entrees():
    print(dedent("""
    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden     
    """))

def desserts():
    print(dedent("""
    Desserts
    --------
    Ice Cream
    Cake
    Pie
    """))

def drinks():
    print(dedent("""
    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears
    """))

appetizers()
entrees()
desserts()
drinks()

def order():
    """
    Asks for a prints a user's order
    """
    print("** What would you like to order? **")
    customer_order = input("> ")
    print(f"You ordered {customer_order}")

    order_dict = {

    }

    ask_again = True
    while ask_again:
        print("Would you like to order more? y or n")
        choice = input("> ")
        if choice == "y":
            print("What would you like to order?")
            customer_order = input("> ")
            print(f"You ordered {customer_order}")
            if customer_order in order_dict:
                order_dict[customer_order] += 1
            else:
                order_dict[customer_order] = 1

        else:
            break
    print(f"The orders are: {order_dict}")

if __name__ == "__main__":
    order()

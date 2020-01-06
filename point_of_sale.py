#need at least three if statements and 3 while loops
#inputs
def get_table_number():
    table_number = int(input("Enter table number: "))
    return table_number

def get_number_of_diners_at_table():
    number_of_diners_at_table = int(input("Enter number of diners at this table: "))
    return number_of_diners_at_table

def get_table_order():
    tax_rate = 1.07
    count = 1
    table_order = 0.00
    diners = get_number_of_diners_at_table()
    table_reciept = ""
    while count <= diners:
        diner_order_price_before_tax = get_diner_order()
        table_order = tax_rate*(table_order + diner_order_price_before_tax)
        diner_reciept_pre_tax= ("Diner" + str(count) + " owes $" + str(round(diner_order_price_before_tax, 2)) + " before tax")
        diner_reciept_with_tax= (" -- owes $" + str(round(tax_rate*diner_order_price_before_tax, 2)) + " after tax")
        table_reciept = table_reciept + "\n" + diner_reciept_pre_tax + diner_reciept_with_tax 
        count += 1
    print(table_reciept)
    print("Table Order Total With Tax: $", round(table_order, 2))

def get_diner_order():
    display_menu_of_food_items()
    #get_menu_item()
    diner_order_item_names = ""
    current_item_name = ""
    diner_order_price_before_tax = 0.00
    while current_item_name != "next":
        diner_order_item_names = diner_order_item_names + current_item_name       
        current_item_name = str(get_menu_item())
        current_item_price = 0.00
        if current_item_name == "Coffee":
            current_item_price = 2.00
        elif current_item_name == "OrangeJuice":
            current_item_price = 3.00
        elif current_item_name == "Bacon":
            current_item_price = 3.00
        elif current_item_name == "next":
            current_item_price = 0.00
        else:
            print("Not a valid Menu Item")
            current_item_price = 0.00       
        diner_order_price_before_tax = diner_order_price_before_tax + current_item_price
                
    return diner_order_price_before_tax

def display_menu_of_food_items():
    item_1_display = "Coffee : $2\n"
    item_2_display = "OrangeJuice: $3\n"
    item_3_display = "Bacon: $1\n"
    item_4_display = "Sausage: $1\n"
    item_5_display = "Pancakes: $2\n"
    item_6_display = "Biscuit $1\n"
    item_7_display = "Hash Browns $1\n"
   
    print("Here are our breakfast menu items:\n",item_1_display,item_2_display,item_3_display,item_4_display,item_5_display,item_6_display,item_7_display)

def get_menu_item():
    menu_item = input("Enter diner's order menu item name, or enter 'next' for next diner: ")
    return menu_item
    
def display_diners_totals():
    #stuck inside get_table_order
    return

def calculate_table_total():
    #stuck inside get_table_order
    return

def display_table_total_info():
    return
    
def main_program(): #needs to accumulate sales for the day and output sales for the day
    #while input(0 !+ quit
    get_table_number()
    #get_number_of_diners_at_table()
    get_table_order()
    return #main_program()

main_program()
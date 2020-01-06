# Write a program to calculate a split restaurant check among any number of friends, including tip. Assume that since you're all friends, it's ok to split the check evenly. 


def calculate_tip_percentage(level_of_service):
    tip_percentage = float(level_of_service) * 0.03
    return tip_percentage

def calculate_tip_total(bill_subtotal, tip_percentage):
    tip_total = bill_subtotal * tip_percentage
    return tip_total

def calculate_tax_total(bill_subtotal, sales_tax_rate):
    tax_total = bill_subtotal * sales_tax_rate
    return tax_total

def calculate_check_total(bill_subtotal, tax_total):
    check_total = bill_subtotal + tax_total
    return check_total

def calculate_per_person_payout_before_tip(check_total, number_of_payers): 
    per_person_payout_before_tip = check_total / float(number_of_payers)
    return per_person_payout_before_tip

def calculate_per_person_payout_towards_tip(tip_total,number_of_payers):
    per_person_payout_towards_tip = tip_total / float(number_of_payers)
    return per_person_payout_towards_tip

def calculate_per_person_total_payout(per_person_payout_before_tip, person_payout_towards_tip):
    per_person_total_payout = per_person_payout_before_tip + per_person_payout_towards_tip
    return per_person_total_payout

def calculate_grand_total_paid_out(per_person_total_payout, number_of_payers):
    grand_total_paid_out = round(per_person_total_payout * float(number_of_payers), 2)
    return grand_total_paid_out

#inputs
bill_subtotal = float(input("Enter bill total before tax and tip: "))
sales_tax_rate = float(input("Enter sales tax rate as a decimal: "))
level_of_service = int(input("Enter level of service on a 1-10 scale: "))
number_of_payers = int(input("Enter number of persons paying: "))

#intermediate calculations/variables
tip_percentage = calculate_tip_percentage(level_of_service)
tip_total = calculate_tip_total(bill_subtotal, tip_percentage)
tax_total = calculate_tax_total(bill_subtotal, sales_tax_rate)
check_total = calculate_check_total(bill_subtotal, tax_total)

#output calculations
per_person_payout_before_tip = calculate_per_person_payout_before_tip(check_total, number_of_payers)
per_person_payout_towards_tip = calculate_per_person_payout_towards_tip(tip_total,number_of_payers)
per_person_total_payout = calculate_per_person_total_payout(per_person_payout_before_tip, per_person_payout_towards_tip)
grand_total_paidout = calculate_grand_total_paid_out(per_person_total_payout, number_of_payers)

# output
print("Bill per person with tax:", "$", per_person_payout_before_tip)
print("Tip per person:", "$", per_person_payout_towards_tip )
print("Total per person:", "$", per_person_total_payout) 
print("Total bill including tax and tip:", "$", grand_total_paidout) 
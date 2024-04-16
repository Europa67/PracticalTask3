# Task 5 - CAPSTONE PROJECT - COMPOUND INTEREST ON A SAVINGS INVESTMENT OR HOME LOAN REPAYMENT

# Note for South African reviewers - a loan to buy a house in the UK is called a mortgage.
# This is close to my heart as I've just bought a house! :-)
# I have taken this into account in naming the variables below. Thanks for your understanding!

import math

print("Welcome to the KalculateInterest programme. This programme will help you calculate investment earnings or mortgage payments.\n")
print("1) Investments - to calculate the amount of interest you'll earn on your savings investment.")
print("2) Mortgages - to calculate the amount you'll have to pay on your home loan.\n")
choice = (input("Please choose between investments or mortgages : ")).lower()

if choice != "investments" and choice != "mortgages":
    print("Invalid input. Please enter investments or mortgages only.")

if choice == "investments":    # SAVINGS INVESTMENT (SIMPLE V COMPOUND INTEREST)
    principal = int(input("Please enter how much you want to save : "))
    rate = int(input("What interest rate are you looking for? "))
    term = int(input("Please state for how long you want to save in years : "))
    print("You want to invest your principal of", principal, "pounds for", term, "years at ", rate, "per cent interest.")
    interest = input("Do you want 1) simple or 2) compound interest? : ").lower()

    if interest == "simple":    # calculate simple interest
        simple = principal * (1 + (rate/100) * (term))
        print("With simple interest at the applied rate and term, your principal would grow to ", simple, "UK Pounds.")
    elif interest == "compound":    # calculate compound interest
        compound = principal * math.pow(1+((rate/100)), term)
        rounded = round(compound, 2)
        print("With interest compounding monthly, your principal would grow to ", rounded, "UK Pounds.")

elif choice == "mortgages":    # HOME LOANS OR MORTGAGES
    house_value = int(input("Please enter the present value of the house : "))
    interest = int(input("Please enter the interest rate product you want : "))
    int_month = (interest/100)/12
    # Issue-1 Changing the requested input from months to years to avoid confusion
    term_yr = int(input("Over what length of time in years do you plan to repay the mortgage : "))
    term = term_yr * 12
    repayment = (int_month*house_value)/(1-(1+int_month)**(-term))
    repay = round(repayment,2)
    print("You will need to pay", repay, "per month, to pay off your mortgage.")

import math

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")
print()

#Variable for the investment type chosen
user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

#If statement for the investment choice, including input from the user on their investment
if user_choice == "investment" or user_choice == "Investment" or user_choice == "INVESTMENT":
    P = float(input("Please enter the amount of money you are depositing: "))
    r = int(input("Please enter the interest rate: "))
    t = float(input("Please enter the number of years you are planning on investing for: "))
    
    interest = input("Please enter the type of interest you'd like; 'simple' or 'compound': ")
 
 #If and elif statements depending on which option the user input above   
    if interest == "simple":
        A = P*(1+ r*t)
    
    elif interest == "compound":
        A = P*math.pow((1+r),t)
    
    else: print("Please enter simple or compound!")
    
    print("The total amount after", t, "years is", A)

#Elif statement for the bond choice, including input from the user on their investment
elif user_choice == "bond" or user_choice == "Bond" or user_choice == "BOND":
    P = float(input("Please enter the present value of the house: "))
    i = int(input("Please enter the interest rate: "))/100/12
    n = int(input("Please enter the number of months over which the bond will be repaid: "))

    repayment = (i * P)/(1 - (1 + i)**(-n))

    print("The repayment after", n, "months is", repayment)
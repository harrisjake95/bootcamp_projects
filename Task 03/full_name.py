#defining the variable asking user to enter their name
name = input("Please enter your full name: \n")

#if statement used to print error message if user enters nothing and asks user to reenter name
if len(name) == 0:
    print("You haven't entered anything.")
    input("Please enter your full name: \n")

#elif statement used to print error message if user enters less than 4 characters and asks user to reenter name
elif len(name) < 4:
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")
    input("Please enter your full name: \n")

#elif statement used to print error message if user enters more than 25 characters and asks user to reenter name
elif len(name) > 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")
    input("Please enter your full name: \n")

#else statement used to print thank you message if user does anything but the above statements
else: print("Thank you for entering your name.")
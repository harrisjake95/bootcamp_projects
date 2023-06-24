#variable for user to enter their swim time
swim_time = int(input("Enter time taken for swimming in minutes: "))
print("Time taken to swim: ", swim_time)

#variable for user to enter their cycle time
cycle_time = int(input("Enter time taken for cycling in minutes: "))
print("Time taken to cycle: ", cycle_time)

#variable for user to enter their run time
run_time = int(input("Enter time taken to run in minutes: "))
print("Time taken to run: ", run_time)

#variable to present the user with their total time
total_time = swim_time + cycle_time + run_time
print("Total time taken for triathlon: ", total_time)

#if statement to display the award for within qualifying time
if (total_time < 100) :
    print("Your award is: Provincial Colours")

#elif statement to display the award for 5 minutes within qualifying time
elif(total_time >100 and total_time <=105) :
    print("Your award is: Provincial Half Colours")

#elif statement to display the award for 10 minutes within qualifying time
elif(total_time >100 and total_time <=110) :
    print("Your award is: Provincial Scroll")

#elif statement to display the award for more than 10 minutes over qualifying time
else:
    print("You have no award")
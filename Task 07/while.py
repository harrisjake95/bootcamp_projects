number = 0
sum_of_numbers = 0
count_of_numbers = 0

#While loop for above variables for user to enter a number 
while number != -1:
    number = int(input("Enter a number: "))
    if number != -1:
        sum_of_numbers = sum_of_numbers + number
        count_of_numbers = count_of_numbers + 1

print("The average of the numbers entered is:", sum_of_numbers/count_of_numbers)
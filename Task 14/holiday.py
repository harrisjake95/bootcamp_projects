#inputs for all the functions from the user
number_of_nights = int(input("Enter number of nights for hotel : "))
city_name = input("Enter city name you are travelling to : ")
number_of_days = int(input("Enter number of days car will be hired : "))

#function that returns the cost of the hotel
def hotel_cost(number_of_nights):
    #choosing price per night as 500
    cost = number_of_nights*500;
    return cost

#function that takes city name as argument and returns the cost of a flights to that city
def plane_cost(city_name):
    if city_name=="paris":
        return 1000
    elif city_name=="singapore":
        return 3000
    elif city_name=="auckland":
        return 4000
    else:
        return 4500

#function that takes number of days input and returns cost of a car
def car_rental(number_of_days):
    #choosing cost of car per day as 300
    cost = number_of_days*300
    return cost

#funtion that takes all arguments and returns the total cost using functions
def holiday_cost(number_of_nights, city_name, number_of_days):
    total_cost = hotel_cost(number_of_nights)+plane_cost(city_name)+car_rental(number_of_days)
    return total_cost

#print hotel cost, plane cost and car rental cost using the functions declared above
print("\nHotel cost : ",end='')
print(hotel_cost(number_of_nights))

print("Plane cost : ",end='')
print(plane_cost(city_name))

print("Car rental cost : ",end='')
print(car_rental(number_of_days))

#function to print the total holiday cost 
print("Total holiday cost : ",end='')
print(holiday_cost(number_of_nights, city_name, number_of_days))
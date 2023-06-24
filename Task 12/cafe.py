#list containing cafe items
menu = ['Sausages', 'Coffee', 'Soup', 'Pizza', 'Breakfast']

#dictionary containing the stock value for each item on the menu list
stock = {'Sausages': 4, 'Coffee': 5, 'Soup': 8,
         'Pizza': 10, 'Breakfast': 10}

#dictionary containing the price value for each item on the menu list
price = {'Sausages': 10.00, 'Coffee': 9.99, 'Soup': 15.0,
         'Pizza': 25.0, 'Breakfast': 12.0}

#total stock worth of cafe items
total_stock = 0.0

#for loop to determine total price of stock
for item in menu:
    #item quantity and cost
    quantity = stock[item]
    cost = price[item]
    #updating total stock with item worth
    total_stock = total_stock + quantity * cost

print('Total stock worth of cafe items: £',total_stock)
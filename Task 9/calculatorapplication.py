#Function to get input from user
def get_input(display: str, to_type: type, on_error: str, validate_func=None):
  while True:
    try:
      value = input(display)
      value = to_type(value)
      if validate_func and not validate_func(value):
        print(on_error)
        continue
      return value
    except ValueError:
      print(on_error)

#Functions for calculations
def add(num1, num2):
  return num1 + num2
def subtract(num1, num2):
  return num1 - num2
def multiply(num1, num2):
  return num1 * num2
def divide(num1, num2):
  if num2 == 0:
    print("\nInvalid operation. You cannot divide by 0.")
  else:
    return num1 / num2

#Operators dictionary for functions
operator_functions = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

error_msg = "Incorrect input. Please try again."

#Ask user input for below option
users_choice = get_input("Enter '1' to enter numbers and operation or '2' to read equations from a txt file: \n", int, "Invalid choice. Try again.", lambda x: x in [1, 2])

#If function where user chooses first choice - ask user to enter numbers and operation
if users_choice == 1:
  num1 = get_input("Enter 1st number:  ", float, error_msg)
  num2 = get_input("Enter 2nd number:  ", float, error_msg)
  operator = get_input("Enter operator (+,-,*,/): ", str, error_msg)
  while True:
    #If function to check if the operator is valid
    if operator not in operator_functions:
        print("Invalid operator. Try again.")
        operator = get_input("Enter operator (+,-,*,/): ", str, error_msg)
    else:
        result = operator_functions[operator](num1, num2)
        print(f"\nResult: {num1} {operator} {num2} = {result}")
        #Write equation to text file
        with open("equations.txt", "a") as file:
          file.write(f"{num1} {operator} {num2} = {result}\n")
          break
#Else if second choice - ask user to enter text file to read equations from
else:
  while True:
    try:
      file_name = input("Enter the name of the file (include file extension .txt): ")
      file_name = open(file_name, "r")
      #Show the lines in text file
      show_lines = file_name.read()
      print(show_lines)
      file_name.close()
      break
    #Produce error if user entered wrong file name
    except FileNotFoundError as error:
      print(f"'{file_name}' does not exist. Try again.")
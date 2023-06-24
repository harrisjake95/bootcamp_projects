# Create a program that allows the user to access 2 different financial calculators
  
* Write the code that will do the following:

  
1. The user should be allowed to choose which calculation they want to do. The first output that the user sees when the program runs should look like this :
investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan
Enter either 'investment' or 'bond' from the menu above to proceed:

2. How the user capitalises their selection should not affect how the program proceeds. i.e. ‘Bond’, ‘bond’, ‘BOND’ or ‘investment’, ‘Investment’, ‘INVESTMENT’, etc., should all be recognised as valid entries. If the user doesn’t type in a valid input, show an appropriate error message.

3. If the user selects ‘investment’, do the following:
   
# Ask the user to input:
* The amount of money that they are depositing.
  
* The interest rate (as a percentage).
  
* The number of years they plan on investing.
  
* Then ask the user to input if they want “simple” or “compound”
interest, and store this in a variable called interest. Depending on whether or not they typed “simple” or “compound”, output the appropriate amount that they will get back after the given period, at the specified interest rate. See below for the formula to be used:
 
* Try entering 20 years and 8 (%) and see what the difference is
depending on the type of interest rate!

* If the user selects ‘bond’, do the following: Ask the user to input:
  
- The present value of the house. e.g. 100000
  
- The interest rate. e.g. 7
  
- The number of months they plan to take to repay the bond. e.g. 120

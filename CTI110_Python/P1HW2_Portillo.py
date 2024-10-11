# CTI110
# P1HW2
# A PORTILLO
# 10/8/2024

'''
3. Ask user to enter their budget
4. Ask user to enter travel destination
5. Ask user for amount they will spend on gas
6. Ask user for amount they will spend on accommodation
7. Ask user for amount they will spend on food
8. Add expenses
9. Subtract expenses from budget
10. Display results
'''
budget = 0.00
gas = 0.00
hotel = 0.00
food = 0.00
budget = 0.00
expenses = gas + hotel + food
balance = gas + hotel + food - budget


print(" Trip Calculator ")
# Ask user to enter their budget
budget = float(input("What is your travel budget? $ "))
# Ask user to enter travel destination
destination = input("Where are you going? ")
# Ask user for amount they will spend on gas
gas = float(input("How much will you spend on gas? $"))
# Ask user for amount they will spend on accommodation
hotel = float(input("How much will you spend on lodging? $"))
# Ask user for amount they will spend on food
food = float(input("How much will you spend on food? $"))
# Add expenses
expenses = gas + hotel + food
# Subtract expenses from budget
balance = budget - (gas + hotel + food)
# Display Results 
print("balance", balance,)

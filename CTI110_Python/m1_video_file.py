'''
--------GETTING INPUT FROM THE USER AND DISPLAYING OUTPUT TO THE SCREEN---------

Allow the user to input information when the program runs
They will type directly into the output screen.
Since we don't know what value they will input, we represent it with a variable

To create a variable:  
    type the name of the variable followed by the assignment operator (=)
    type the value associated with that variable.
    If you want to ask the user to enter information, use the input() function
    as the value. You must always pass a string to the input function explaining
    to the user what information you want them to input.
    
To display info to screen, use the print() function
You can pass a series of strings and/or variables to the print function
Separate strings and variables with a comma
'''

###Example of "hard coding" a value into a variable
##city = "Fayetteville"
##
###Example of getting input from the user
##
##day_of_week = input("What day of the week is today? ")
##
##weather = input("How is the weather today? ")
##
##print("Today is", day_of_week, "and the weather is", weather, "in", city)



'''
--------CONVERTING VALUES TO DIFFERENT DATA TYPES---------
string: what we have used so far. Seen as a collection of letters and symbols. Cannot be used for math.
integer: whole number. No places after the decimal are allowed. Can be used in math expressions
float: number with places after the decimal. Can be used in math expressions
bool: must be one of two options: True or False   No other values are allowed. No quotes around values
'''



###Example of converting a variable to an integer
##age = input('How old are you?')
##
##print(type(age))
##
###Convert age to an integer
##age = int(age)
##
##print(type(age))
##
###Calculation
##older_age = age + 10
##
###Display info to user
##
##print("You are", age, "years old.")
##print("In ten years, you will be", older_age)


#Example of convering a variable to a float
ounces = input("How many ounces of apples do you have?")

ounces = float(ounces)


#Find conversion rate for ounces to pounds. Convert from ounces to pounds.
pounds = ounces / 16

#Display the results
print("You have", pounds, "pounds of apples.")

#Example of creating a bool variable. Not usually used with input function. Used to create program logic

#logged_in = True
#print("User currently logged in....", logged_in)


#Printing symbols to the screen.
#Less than greater than. Simple math
#DO THIS TOGETHER -




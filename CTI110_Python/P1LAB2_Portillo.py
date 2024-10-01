# CIT 110
#P1LAB22 - Receipt
#Portillo
#10/1/24


print("P1LAB2")
#For today, let's do a resturant
#that only sells burgers and fries

#declare our variabes
num_burgers = 0
num_fries = 0
burger_cost = 4.99
fry_cost = .99

print("Can I take your order?")
#we have to convert the input to an int
num_burgers = int(input("how many burgers?"))

print("you ordered", num_burgers, "burgers")

num_fries = int(input("How many fries?"))
print("Ok, Thats", num_fries, "french fries.")

burger_total = num_burgers * burger_cost
fry_total = num_fries * fry_cost
meal_total = burger_total + fry_total
#print the receipt
print("-" * 20)
print(num_burgers,"burger\t$", burger_total)
print(num_fries,"fry\t\t$", fry_total)
print("-" * 20)
print("total\t\t$", meal_total)





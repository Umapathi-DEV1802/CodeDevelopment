# The 'Hello World!' is String with  group of characters.
# print("Hello World!")

# # Challenge
# print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.\n2. Knead the dough for 10 minutes.\n3. Add 3g of Salt.\n4. Leave to rise for 2 hours.\n5. Bake at 200 degrees C for 30 minutes.")


# print(len(input("What is your name? ")))

# glass1 = "milk"
# glass2 = "juice"
# a=glass1
# b=glass2
# glass2=a
# glass1=b
# print(glass1)
# print(glass2)

# City_Name=input("What is the city you grow up?\n")
# Pet_Name=input("What is your pet name?\n")
# print("The band name was " + City_Name + " " + Pet_Name)

# Subscripting

#print(f"Number of letters in your name: {len(input("Enter your name? "))}")

# print(3*3/3+3-3)

#PEMDAS
# Parenthesis, Exponential, Multiplication, Divide, Addition, Subtraction

# print("Welcome to the tip calculator")
# Total_Bill =float(input("What was the totalbill? $\n"))
# Tip = int(input("How munch tip would you like to give? 10, 12, or 15?\n"))
# Number_of_People = int(input("How many people to split the bill?\n"))
# Each_person_Share = (Total_Bill*(1+Tip/100)/Number_of_People)
# print(f"Each person should pay: ${round(Each_person_Share,2)}")

# Vedio 23 was completed of the Day 3

# weight = 85
# height = 1.85

# bmi = round(weight / (height ** 2),2)

# 🚨 Do not modify the values above
# Write your code below 👇

# if bmi < 18.5:
#     print(f"underweight {bmi}")
# elif bmi >= 18.5:
#     print(f"normal weight {bmi}")
# elif bmi >= 25:
#     print(f"overweight {bmi}")

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
# S = 15
# M = 20
# L = 25 
# pepperoni_small_pizza = 2
# pepperoni_medium_Large_pizza = 3
# extra_cheese_Price = 1

# if size == "S":
    # bill = 15
    # if pepperoni == "Y":
        # bill+= 2
#     elif extra_cheese == "Y":
#            bill+= 1
#     print (f"Your Final bill for Pizza: ${bill}")
# elif  size == "M":
#     bill = 20
#     if pepperoni == "Y":
#         bill+= 3
#     elif extra_cheese == "Y":
#             bill+= 1
#     print (f"Your Final bill for Pizza: ${bill}")
# elif size == "L":
#     bill = 25
#     if pepperoni == "Y":
#         bill+= 3
#     elif extra_cheese == "Y":
#           bill+= 1
#     print (f"Your Final bill for Pizza: ${bill}")
# else:
#     print("Please select the choice as indictaed above")

# username = input("What is your name?")
# length = len(username)
# print(username + " " + str(length))

# print(str(len(input("What was your Baby Name?"))))

# Simplified 4 lines of code to single line

# print("Welcome to the Band Name Generator.\n"+"Your band name could be: "+input("Which city did you grow up in?\n")+" "+input("What is the name of your Pet\n"))

# print(type(len(str(123456))))
# print(type(str(123456)))
# print(type(123.456))

# print("Numberof letters in your name: " + str(len(input("Enter Your Name\n"))))

# print(3+3*3/3-3)

# bmi=84/1.65**2
# print(round(bmi,2))

print("Welcome to the Tip calculator!")

Total_Bill = float(input("What was the total bill? $"))

Percentage_of_Tip = (int(input("What percentage of tip would you like to give? 10, 12, or 15?\n"))/100)*Total_Bill

Split_Bill = int(input("How many people to split the bill?\n"))

Final_Bill_Split = round(float(((Total_Bill + Percentage_of_Tip)/Split_Bill)),2)                 

print(f"Each person should pay: ${Final_Bill_Split}")
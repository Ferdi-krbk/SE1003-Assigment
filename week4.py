"""
how_much = int(input("How much money in your bank account? :"))
real_estate = int(input("How much houses do you have in Kötekli? :"))
car = (input("Do you have a car? :"))

threshold_money = 100_000
threshold_house = 5

if how_much > threshold_money and real_estate > threshold_house:
    if car == "yes" or car == "Yes":
        print("You don't have to all day work")
    else:
        print("You have to buy a car.")

elif how_much > 50000 and car == "Yes" or car == "yes":
    print("You have to work one day at week")

else:
    print("You are so poor, you have to work for live.")
"""


"""
hp greater than 60 less than 75 200.000
if greater than 75 less then or equal 90 350.000
if greater than 90 less than or equal 110 500.000
if greater than 110 less than or equal 150 700.000
if greater than 150 less than or equal 200 1.200.000
otherwise 2.000.000
"""

hp = int(input("What is the hp of the car that you wanted? :"))

if hp <=60:
    print("We don't have any car below with that horse power.")
elif  60 < hp <= 75:
    print("The cost of the car is 200.000 Turkish Liras.")
elif 75 < hp <= 90:
    print("The cost of the car is 350.000 Turkish Liras.")
elif 90 < hp <= 110:
    print("The cost of the car is 500.000 Turkish Liras.")
elif 110 < hp <= 150:
    print("The cost of the car is 700.000 Turkish Liras.")
elif 150 < hp <= 200:
    print("The cost of the car is 1.200.000 Turkish Liras.")
else:
    print("The cars that have this horse power costs 2.000.000 Turkish Liras")
        
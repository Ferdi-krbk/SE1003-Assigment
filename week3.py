"""for j in range(0,101,2):
    print(j)
"""
"""
for i in range(0,101):
    if i % 2 != 0:
        print(i) 
"""
"""
for i in range(0,101):
    if i % 2 != 0:
        continue
    print(i)
"""
"""  
for i in range(0,101):
    if i % 2 != 0:
        print(i) 
"""     
"""
number = 0

while  number<=100:
    print(number)
    number = number + 2

number = 0
while True:
    if number % 2 == 0:
        print(number)
    number = number + 1
    if number == 101:
        break
number = 0 
print("Number: ", number)
while number<= 100:
    if number % 2 != 0:
        print(number)
    number += 1


students= ["Ahmet","Onur","Mehmet","Enes","OÄŸuz"]
for name in students:
    if name == "Mehmet":
        print(name ,  " : ", 100)
    else:
        print(name ,  " : ", 50)

for i in range(1, 10):
    if i >= 5:
        continue
    print(i)


for i in range(1, 4):
    for j in range(1, 4):
        for z in range(1,4):
            print(f"({i}, {j}, {z})", end=" ")
  
    print()

"""
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} =  {i * j}", end="\t")
    print()
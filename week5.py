"""
def myAbs(number):
    if number < 0:
        print("Above")
        return -number
    print("Below")
    return number
myAbs(-5)    

"""
"""
def myAbs(number):
    if number < 0:
        print(-number)
    else:
        print(number)    

myAbs(-10)
"""

"""
def myAbs(number):
    if number < 0:
        return -number
    return number

print(myAbs(-10))
"""

"""
def tcvalidity(tc):
    a_11 = tc // 10**10
    a_10 = tc // 10**9
    a_9 = tc // 10**8
    a_8 = tc // 10**7
    a_7 = tc // 10**6
    a_6 = tc // 10**5
    a_5 = tc // 10**4
    a_4= tc // 10**3
    a_3 = tc // 10**2
    a_2 = tc // 10
    a_1 = tc % 10    
    ilk10toplam = a_11+a_10+a_9+a_8+a_7+a_6+a_5+a_4+a_3+a_2
    sonrnakam = ilk10toplam % 10
    if a_11 == 0:
        print("Error, first digit can't be 0.")
    elif sonrakam == a_1:
        print("Your ID is valid.")
    else:
        print("Your ID is not valid.")
    


tcvalidity(int(input("Write Your ID Please:")))


"""
"""
def tcvalidity(tc):
    if tc // 10**10 == 0:
        print("Error, first digit can't be 0.")
    
    toplam = 0
    ilk10 = tc // 10 
    for _ in range(10):
        toplam += ilk10 % 10
        ilk10= ilk10 //10

    if toplam %10 == tc % 10:
        print("Your ID is valid.")
    else:
        print("Your ID is not valid.")
tcvalidity(int(input("Write Your ID Please: ")))
"""
"""
result = ""
if 10 < 5:
    result = "True"

else:
    if 1 == 1:
        result = "Equal"
    else:
        result = "False"
print(result)

result = "True" if 10<5 else "Equal" if 1 == 1 else "False"
print(result)

"""

#we will implement function that five parameter its check whether two of these numbers are equal or not
#5 sayılı fonksiyon 5 sayıdan 2 tanesi eşit mi diye bakıcak eşit sayı var yada eşit sayı yok dicek

"""
print("A"+" B"+" "+"C")
print("1"+" "+"2")

number1=4
number2=5
total = number1 + number2

#4 + 5 = 9

notFormattedString= str(number1)+ " + " + str(number2) + " = " + str(total)
formattedString= f"{number1} + {number2} = {total}"
formattedString2 = "{} + {} = {}".format(number1,number2,total)
print(notFormattedString)
print(formattedString)
print(formattedString2)
"""
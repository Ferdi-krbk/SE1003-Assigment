"""
value = int(input("Give Number: "))

def triangle_func(value):
    if value == 1:
        return 1
    result = 0
    for i in range(0,value+1):
        result = result + i
    return result


print(triangle_func(value))

"""

"""
value = int(input("Give Number: "))
def triangle_func(value):
    if value == 1:
        return 1
    result = 0
    while value >= 0:
        result+= value
        value-=1
    return result

print(triangle_func(value))
"""
"""
value = int(input("Give Number: "))
def triangle_func(value):
    if value <=0:
        return("Number can't be negative or 0")
    if value == 1:
        return 1
    else:
        return triangle_func(value-1)+value
    
print(triangle_func(value))
"""
"""
def zero_to_hundred(first,last):
    if first == last:
        print(first , end=" ")
    else:
        print(first, end=" ")
        return zero_to_hundred(first + 1 ,last)

zero_to_hundred(0,100)

"""
def zerotohundred(first,last):
    if last == 11:
        return 
    else:
        print(first + last)
        return zerotohundred(first+1,last+1)

zerotohundred(0,1)
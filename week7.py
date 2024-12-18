integer_list = [0,1,2,3,10,4,5]
empty_list=[]
mix_types = [1,"string",True,32.48,{2},[1,2,3],range(1,5),{"name" : "Jonni"}]
for i in mix_types:
    print(type(i))

nested_list = [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[8]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

m3triks = [
    {1,2,3},
    {4,5,6},
    {7,8,9}
]
for i in m3triks:
    print(f"{i}\n")

integer_list = [0,1,2,3,10,4,5]
print(integer_list[6])
integer_list = [0,1,2,3,10,4]
#print(integer_list[6])
print(integer_list[-1])

first_four = integer_list[0:4]
print(first_four)
first_four= integer_list[ :4]
print(first_four)
print(integer_list[4:])

original_list = [1,2,3,4,5,6]
new_list = original_list[:]
new_list = original_list[:5]
print(new_list)
print(original_list)


fruits = list()
print(fruits)
fruits.append("Banana")
print(fruits)
fruits.append("Cherry")
print(fruits)
fruits.insert(1,"Strawberry")
print(fruits)
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
fruits.insert(0,"Apple")
print(fruits)
fruits.reverse()
print(fruits)
fruits.append("Cherry")
print(fruits)
print(fruits.index("Cherry"))
print(fruits.count("Cherry"))
int_list = [0,1,2,3,4,5,6,7,8,9]
print(int_list[::-1])

for i in range(len(fruits)):
    print(fruits[i])
print()
for fruit in fruits:
    print(fruit)

def meyve():
    fruits = ["Banana","Cherry","Strawberry","Apple","Cherry"]
    counter = 0
    for fruit in fruits:
        if fruit == "Cherry":
            counter+=1
    return counter
print(meyve())


def meyve_2():
    fruits = ["Banana","Cherry","Strawberry","Apple","Cherry"]
    counter = 0
    target = input("Meyve nedir?")
    for fruit in fruits:
        if fruit == target:
            return 1
    return None
            
print(meyve_2())


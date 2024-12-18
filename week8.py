import random
"""
casting = tuple([1,2,3,4,5])
emptyTuple = ()
emptyTuple = tuple()
myTuple = (1,2,3,4,4,5)
print(type(casting))
print(myTuple.index(3))
print(myTuple.count(4))
"""
"""
def biggestdifference():
    sicakliklar= []
    """
"""
    for b in range(30):
        sicakliklar.append(random.randint(0,35))
    ensicak = 0
    for sicaklik in sicakliklar:
        if sicaklik> ensicak:
            ensicak = sicaklik

    print("En yüksek sicaklik: ",ensicak)
    maksindex = sicakliklar.index(ensicak)
    maksfark = 0
    for i in range(maksindex,len(sicakliklar)-1):
        fark= abs(sicakliklar[i] - sicakliklar[i+1])
        if maksfark < fark:
            maksfark = fark
    print("En büyük fark:",maksfark)
        

biggestdifference()
"""
isAdam= input("Are you adam?")
number = random.randint(0,1000)
guess = int(input("Please give a number to guess: "))
counter = 1

if isAdam == "Y" or isAdam == "y":    
    while guess != -1  and number != guess and counter <10:
        counter += 1
        
        if number < guess:
            print("Your guess is bigger than number.")
        else:
            print("Your guess is lower than number.")
        guess = int(input("Please give a number to guess :"))

if guess == -1:
    print("Thanks for playing.")
if counter == 10:
    print("You lost the game.Number was :",number)
if guess == number:
    print("You win the game.")
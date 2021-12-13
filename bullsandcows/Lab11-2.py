import random

randomnumber = str(random.randint(1000, 9999))
print(randomnumber)
randomnumberlist = []
cow = 0
guestcount = 0

for i in randomnumber:
    randomnumberlist.append(i)

while cow < 4:
    guestnumber = input("Enter a Number :")
    guestnumberlist = []
    cow = 0
    bull = 0
    guestcount += 1
    for i in guestnumber:
        guestnumberlist.append(i)
    for i in randomnumberlist:
        if i in guestnumberlist and randomnumberlist.index(i) == guestnumberlist.index(i):
            cow += 1
        if i in guestnumberlist and randomnumberlist.index(i) != guestnumberlist.index(i):
            bull += 1
    print("Cow: ", cow, " | ", "Bull: ", bull)
print("You find the random number(", randomnumber, ") in ", guestcount, "guess")




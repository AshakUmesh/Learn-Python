import random

alphabetlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numberlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
symbollist = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

print("Welcome to PyPassword Generator")
alpnum = int(input("How many letters would you like in your password? "))
symnum= int(input("How many symbols would you like? "))
num = int(input("How many numbers would you like? "))

total = alpnum+ symnum+ num
newlist = []

for i in range(alpnum):
    x=random.choice(alphabetlist)
    newlist.append(x)

for i in range(symnum):
    y=random.choice(symbollist)
    newlist.append(y)

for i in range(num):
    z=random.choice(numberlist)
    newlist.append(z)

print(f"\n{newlist}",end="")

print("\n\nYour password is:  ",end="")

for j in range (total):
    a=random.choice(newlist)
    print(a,end="")
print("\n\n")


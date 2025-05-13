import List
def encode(msg ,n):
    temp=""
    for char in msg:
        if char in List.alphabetlist:
            index=(List.alphabetlist.index(char)+n)%26
            temp+=List.alphabetlist[index]
        else:
            temp+=char
    print(temp)

def decode(msg,n):
    temp = ""
    for char in msg:
        if char in List.alphabetlist:
            index = (List.alphabetlist.index(char) - n) % 26
            temp += List.alphabetlist[index]
        else:
            temp += char
    print(temp)

con="yes"



while con=="yes":
    choice = input("Type 'encode' to encrypt , type 'decode' to decrypt ")

    message = input("Type your message: ")
    shift = int(input("Enter the shift number: "))

    if(choice=="encode"):
        encode(message,shift)
    elif(choice=="decode"):
        decode(message,shift)

    con=input("Type 'yes' if you want to continue otherwise type 'no'")





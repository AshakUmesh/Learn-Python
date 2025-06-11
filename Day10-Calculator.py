def add(num1,num2):
    """This funtion is used to add two number"""
    return num1+num2
def sub(num1,num2):
    """This funtion is used to subtract two number"""
    return num1-num2
def mul(num1,num2):
    """This funtion is used to multiply two number"""
    return num1*num2
def div(num1,num2):
    """This funtion is used to divide two number"""
    return num1/num2

cont="y"
num1=int(input("What is the first number? "))

while cont =="y":

    print("+\n-\n*\n/")
    opr=input("Pick an operation :  ")
    num2=int(input("What is the next number? "))

    if opr=="+":
        final=add(num1,num2)
    elif opr == "-":
        final=sub(num1, num2)
    elif opr=="*":
        final=mul(num1,num2)
    elif opr=="/":
        final=div(num1,num2)

    print(f"{num1} {opr} {num2} = {final}")
    cont=input(f"type 'y' to continue calculating with {final}  or type 'n' to start a new calculation  ")

    if cont=="y":
        num1=final



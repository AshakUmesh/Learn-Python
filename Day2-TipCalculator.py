print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much % tip would you like to give? 10 ,15 ,20 ? "))
num = int(input("How many people to split the bill "))
totalbill = ((bill*tip)/100)+bill
amount = totalbill/num
print(f"Each person should pay: $ {amount}")

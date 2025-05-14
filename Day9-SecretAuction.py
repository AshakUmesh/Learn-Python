print("Welcome to the secret auction program. ")
cont = "yes"
content={}

while cont == "yes":
    name=input("What is your name?:  ")
    bid=int(input("What is your bid?: $"))
    content[name]=bid
    cont=input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

key=max(content ,key=content.get)
winningbid=content[key]
print(f"\nThe winner is {key} with a bid of ${winningbid}. ")
from random import choice

drinks = ["vodka" , "wiskey" , "gin" , "tequila" , "rum" , "rakia" , "sake"]
print(drinks)
print("Welcome to the virtual pub")
name = input("I am the bartender, how do I call you? ")
try:
    age = input(f"How ald are you, {name}? ")
    age = int(age) #try to convert to a number
    if age >= 21 :
        legal = True
    elif age < 16:
        legal = False
    else:
        country = input(f"Where are you from, {name} ")
        legal = False
        if age >= 21:
          legal = True
        elif age >= 18 and country != "USA":(
            legal) = True
        elif age >= 16 and country == "Luxembourg":\
             legal = True
    if legal:
        print("You are allowed to drink")
        print(f"Here is a {choice(drinks)} for you")
    else:
             print(f"Dear {name}, unfortunately you are not allowed to drink")
except ValueError:(
              print("Please give a valid age"))

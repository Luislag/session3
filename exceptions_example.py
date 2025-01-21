name = input("What is your name? ")
print("Hello" , name )
age = input("How old are you? ")
try:
    # another way to format print is via f-strings
    print(f"{name}, you were born in {2024 - int(age)}")
except ValueError:
    print("Age must be a valid number")
    print(f"The value that you typed was {age}")
except ZeroDivisionError:
    print("You cant divide by zero")
except:
    print("No idea what else can go wrong, but just in case")
else: # in case no exceptio happened
    print("Thanks for being a good sport and not trying to crash the game")
print("Thanks for playing")
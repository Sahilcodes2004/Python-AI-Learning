import random
x = int(input("Enter a number: "))
number=[1,2,3,4,5,6,7,8,9,10]
guess=random.choice(number)
print("Random number:", guess)
if(x==guess):
    print("You guesses correctly !")
else:
    print("wrong guess")
    print(f"You entered {x}")
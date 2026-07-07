import random
import string
s=input("Enter you secret message")
x=len(s)
b=""
if(x<3):
    dec=s[::-1]
else:
    a=s[0]
    b=s[1:]+a
    
    charpool=string.digits+string.ascii_letters
    z=""
    for i in range(4):
        rand_char=random.choice(charpool)
        z=z+rand_char
    z=z+b+z
    print("The Decoded Message is ",z)
import random
import string

s = input("Enter your secret message: ")
x = len(s)

if x < 3:
    result = s[::-1]
else:
    a = s[0]
    b = s[1:] + a
    
    charpool = string.digits + string.ascii_letters
    z = ""
    for i in range(4):
        rand_char = random.choice(charpool)
        z += rand_char
    
    result = z + b + z

print("The Encoded Message is:", result)   
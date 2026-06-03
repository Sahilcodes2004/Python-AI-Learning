  

age=6
if age>=18:
    print("you are adult")
elif age >=12:
    print("you are a teenager")
elif age<12:
    print("you are a child")
else:
    print("you are ababy")
def is_adult(age):
 if age>18:
    return "adult"
 else:
    return"not an adult"
x=29
print(is_adult(x))
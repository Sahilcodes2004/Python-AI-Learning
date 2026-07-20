a=input("Enter the number")

try:
    print(f"The multipliaction table of {a} is:")
    for i in range(1,11):
     print(f"{int(a)} X {i} ={int(a)*i}")
except Exception as e:
     print("INVALID INPUT!")

try:
   x=int(input("Enter the number"))
   for i in range(x,-1,-1):
      y=x/i
      print(y)
   a=[3,4,5]
   print(a[8])
except IndexError:
   print("Index Not Found!")
   
except ZeroDivisionError:
    print("Division by Zerro Error Occured")
finally:
   print("Hope u got your answer")

b = input("Enter the number: ")

if b == "quit":
    raise ValueError("Everything is stopped.")

try:
    b = int(b)
    print("You entered:", b)
except ValueError:
    raise ValueError("Please enter a valid integer or 'quit'.") 
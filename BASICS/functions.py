def agegroup(age):
    if age<=12:
        return ("You are a child")
    elif 12<age<=18:
        return ("You are a teenager")
    elif 18<age<=60:
        return("You are a adult")
    else:
        return("You are a senior citizen")
 
def credential(name,age):
    print (f"Your name is {name} and you are {age} years old")

def mean():
    x=input("the")
    pass#used for future modifications in a function you can leave your function in middel of is cretaion


x=input("Enter your name:")
age=int(input("Enter your age:"))
credential(x,age)
res=agegroup(age)
print(res)
#function arguments
def average(a,b):
    return("The average is ",(a+b)/2)
c=average(3,6)
print(c)
def average(a=1,b=9):#default arguments
    print("The average is ",(a+b)/2)
average(2)
def name1(fname,mname="amy",lname="watson"):#fname and mname are required arguments
    print("Hello,",fname,mname,lname)
name1("lim","geowne")
#variable-length arguments
def avg(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("Average is:",sum/len(numbers))
avg(10,2)
#keyword arbitarty arguments
def name(**name):
    print("hello",name["fname"],name["mname"],name["lname"])
name(mname="kumar",lname="sami",fname="kim")

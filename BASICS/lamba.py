#lambda functions
from functools import reduce
lambda num:num*2
multiply=lambda a,b:a*b
print(multiply(2,3))

#map(),fileter(), reduce()

number=[1,4,6]
def double(a):
    return a*2
result=map(double,number)
print(list(result))
#map
vari=[2,4,8]


result=map(lambda a:a*2,vari)
print(list(result))

#filter
nami=[1,3,5,4,8,9,44]


result=filter(lambda n:n%2==0,nami)
print(list(result))

#reduce
expenses=[('dinner',90),('carrepair',500)
          ]
sum=reduce(lambda a,b:a[1]+b[1],expenses)
print(sum)



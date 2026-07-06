condition=0
while condition<10:
    print("The condition is True")
    condition+=1

items=[1,2,3,4]


for item in items:
    if item==2:
     continue
    print(item)


for i in range(11):
   print(i*i)
else:
   print("Square of first 10 numbers")
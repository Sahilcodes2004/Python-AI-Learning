animals=["dog","cat","cow"]
print(animals)
animals.append("buffalo")#used to add one element to last ofthr list
print(animals)
animals.extend(["lion","tiger"])#used to ad list to the end of list
print(animals)
print(len(animals))
print(animals[1:3])
print(animals[-4:-2])#len(animals)-4:len(animals)-2=2:4
print(animals[2])
if "cowo" in animals:
    print("hurah")
else:
    print("cowo not in animals")
print(animals[0:5:2])#step up in list slicing is used to skip certain item by jumping forward by the given number 

#list comprehension is used to creat new lists from other iterables like lists,tuples,dictionaries,sets,and even in arrays and strings

lst=[i*i for i in range(11)]
print(lst)
lst2=[i for i in range(11) if i%2==0]
print (lst2)
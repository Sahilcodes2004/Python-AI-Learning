dogs=["pomerian","labrador",2.5,1,"cat","python",34.9]
print(dogs)
print("umber"in dogs)
print(dogs[1])
print(dogs[-1])
print(dogs[2:])
print(dogs[:2])
print(len(dogs))
(dogs.append("sahil"))#add new element to a list
dogs.extend(["Judah","Carina"])#combine multiple lists
dogs+=[123,"rome"]
print(dogs)
dogs.remove(123)
print(dogs)
dogs.pop()#removes the last added element from the list

items=["sam","cat"]
items.insert(3,"luna")
print(items)
items[1:1]=["Sea","def"]
print(items)
items.sort()
print(items)
sorted(items,key=str.upper)
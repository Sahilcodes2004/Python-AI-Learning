#Tuples are immutable once created can't be modified
tup=(1,2,3,"sahil")
print(tup)
print(type(tup))
print(tup[0])
print(tup[3])
print(len(tup))
if 2 in tup:
    print("2 is present in tup")
tup2=tup[1:len(tup)]
print(tup2)
print(tup2[:2])


#tuples methods
countries=("india","Russia","africa")
temp=list(countries)
temp.append("America")#add item
temp.pop(1)#remove item 
temp[2]="finland"#chnage item 
countries=tuple(temp)
print(countries)
 
tp=(2,3,4)
pt=(5,2,6,7)
st=tp+pt
print(st)
print(st.count(2))
print(st.index(2))
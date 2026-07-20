names={"harsh","carina","iliese","leevan","sahil","sahil"}
print(names)
harry=set()
print(type(harry))

for value in names:
    print(value)


#sets methods

#union
s={1,2,3,4,5}
s1={"sahil","kim","sam"}
s2={6,7,8,9,10,"sahil"}
print(s.union(s2))

#update()
s.update(s1)
print(s)


#intersection
s3=s2.intersection(s)
print(s3)

print(s.intersection_update(s2))

#symmetric differnce
s4=s1.symmetric_difference(s)
print(s4)
print(s3.isdisjoint(s2))

#subset 
print(s1.issubset(s1))

#superset
print(s1.issuperset(s))

#remove/discard
s1.remove("sahil")
print(s1)
#discard does noy pops an error if element is present in the set
s1.discard(1)
print(s1)

#del is used to delete th entire set 
#del s
#print(s)

s.clear()
print (s)
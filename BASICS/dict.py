# dictionaries used to create a key value pair
dict={"sahil":24,"sam":28,"cam":12,"umber":90}
print(dict)
print(dict.get("sam"))
dict.pop("sahil")

print(dict)
{"cam":12,"umber":90}
print(dict.keys( ))
print (dict)
dict["hina"]=23
print(dict)
dict.pop("hina")
print(dict)
del dict["umber"]
print(dict.values())
dict.update({"elay":34})
for key, value in dict.items():
    print(f"The value coresponding to the {key} is {value}")
#dict.clear()

del dict["sam"]
print(dict)

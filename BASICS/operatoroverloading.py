class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __gt__(self, other):
     return True if self.age>other.age else False
roger=Dog("sahil",22)
sam=Dog("syd",121)
print(roger>sam)
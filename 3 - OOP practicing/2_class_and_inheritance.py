#Creating an animal class

class Animal(object):
    
    alive = True

    def __init__(self, age):
        self.age = age
        self.name = None
        

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name
    
    def set_age(self, newAge):
        self.age = newAge

    def set_name(self, newName = ""):
        self.name = newName

    def __str__(self):
        return f"{self.name} is {self.age} years old."


class Cat(Animal):

    def __init__(self, age, name, parent1 = None, parent2 = None):
        Animal.__init__(self, age)
        self.name = name
        self.parent1 = parent1
        self.parent2 = parent2

    def meow(self):
        return print("meow")
    
    def get_parent1(self):
        return self.parent1
    
    def get_parent2(self):
        return self.parent2

    def __str__(self):
        return f"cat: {self.name} is {self.age} years old."
    
    def __add__(self, other):
        return Cat(0, "newborn" , self, other)
    
    def __eq__(self, other):
        if self.parent1.name == other.parent1.name and self.parent2.name == other.parent2.name:
            return "Parents are same"
        else:
            return "NADA QUE VER"

pater = Cat(5, "pater" , "Hector", "Jorgelina")
mater = Cat(3, "mater", "Eric", "Ruby")
thirdcat = Cat(5, "Lolo", "Pedro", "Lara")

newcat = pater + mater
secondnewcat = pater + mater
thirdnewcat = pater + thirdcat

print(newcat, newcat.get_parent1(), newcat.get_parent2())
print(newcat == secondnewcat)
print(secondnewcat == thirdnewcat)







class Person(Animal):
    def __init__(self, age, name):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friendsList = []

    def addFriend(self, friend):
        self.friendsList.append(friend)

    def get_friends(self):
        return self.friendsList
    
    def __str__(self):
        return f"Person: {self.name} is {self.age} years old."
    

class Student(Person):
    def __init__(self, age, name, major = None):
        Person.__init__(self, age, name)
        self.major = major

    def set_major(self, major):
        self.major = major

    def get_major(self):
        return self.major
    
    def __str__(self):
        return f"Student: {self.name} is {self.age} and Major: {self.major}."
    

#Class variables are shared across all instances



# manolette = Student(31, "Manuel")
# print(manolette)
# manolette.set_major("Arlet")
# print(manolette.alive)



# manuel = Person(31, "Manuel")

# print(manuel)
# manuel.addFriend("Pedro")
# print(manuel.get_friends())
# manuel.addFriend("Carlos")
# print(manuel.get_friends())
# manuel.addFriend("Julian")
# print(manuel.get_friends())
    
# lolo = Animal(4)
# puto = Animal(5)
# lolo.size = "Huge"
# print(puto)
# print(lolo)
# lolo.set_age(10)
# print(lolo)
# lolo.set_name("Lolo")

# lolo.age = "Infinite"
# print(lolo)
# print(lolo.size)

# catty = Cat(2)
# catty.meow()
# catty.set_age(100)
# print(catty)
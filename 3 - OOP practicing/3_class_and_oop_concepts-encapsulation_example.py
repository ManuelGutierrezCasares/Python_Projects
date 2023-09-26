#Private don't really work in Python, as you can access the value doing object._class__attribute; usage is sort of a guide for other devs that will work on your code

class Character:
    def __init__(self, name ="Default", strength = 10, intelligence = 10, defense = 10, life = 100):
        self.__name = name
        self.__level = 1
        self.__strength = strength
        self.__intelligence = intelligence
        self.__defense = defense
        self.__life = life
        self.__turno = False
        

    def checkAttributes(self):
        print("Character Name: ", self.__name)
        print("-Level: ", self.__level)
        print("-Strength: " , self.__strength)
        print("-Intelligence: " , self.__intelligence)
        print("-Defense: " , self.__defense)
        print("-Life: " , self.__life)


    def levelUp(self, strength, intelligence, defense):
        self.__level = self.__level + 1
        self.__strength = self.__strength + strength
        self.__intelligence = self.__intelligence + intelligence
        self.__defense = self.__defense + defense

    def isAlive(self):
        if self.__life > 0:
            return True
        else:
            return False
        
    def __die(self):
        self.__life = 0
        print(self.__name, "is dead.")

    def damage(self, enemy):
        return self.__strength - enemy.__defense
    
    def attack(self, enemy):
        damage = self.damage(enemy)
        enemy.__life = enemy.__life - damage
        print(self.__name, "has done ", damage, " points to ", enemy.__name)
        if enemy.isAlive():
            print(enemy.__name, "has now: ", enemy.__life, " life")
        else:
            enemy.__die()

    def getStrength(self):
        return self.__strength
    
    def setStrength(self, strength):
        if strength < 0:
            print("Error, has introducido un valor negativo")
        else:
            self.__strength = strength


#Check if default values are working...
##jhonny = Character()
##jhonny.checkAttributes()

#Check if correct values are working
jhonny = Character("Jhonny", 10, 5, 10)
##jhonny.checkAttributes()

#Leveling up
jhonny.levelUp(10, 5, 10)
##jhonny.checkAttributes()

#Checking if isAlive
##print("Jhonny is alive: ", jhonny.isAlive())

#Character Dieing
##jhonny.die()
##jhonny.checkAttributes()
##print("Jhonny is alive: ", jhonny.isAlive())

#Create second character to play with
goro = Character("Goro", 50, 1, 10)
##goro.checkAttributes()

#First character attacks second one
jhonny.attack(goro)
goro.checkAttributes()


#Trying to access and use methods / attributes when private
##jhonny.strength = 10000
##jhonny.__die()

#Using getters and setters
##print(jhonny.getStrength())
##jhonny.setStrength(1000)
##print(jhonny.getStrength())

#Example to access "encapsulated" / "private" methods or attributes
jhonny._Character__strength = 500
jhonny._Character__die()
jhonny.checkAttributes()
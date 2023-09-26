class Character:
    def __init__(self, name ="Default", strength = 10, intelligence = 10, defense = 10, life = 100):
        self.name = name
        self.level = 1
        self.strength = strength
        self.intelligence = intelligence
        self.defense = defense
        self.life = life
        self.turno = False
        

    def checkAttributes(self):
        print("Character Name: ", self.name)
        print("-Level: ", self.level)
        print("-Strength: " , self.strength)
        print("-Intelligence: " , self.intelligence)
        print("-Defense: " , self.defense)
        print("-Life: " , self.life)


    def levelUp(self, strength, intelligence, defense):
        self.level = self.level + 1
        self.strength = self.strength + strength
        self.intelligence = self.intelligence + intelligence
        self.defense = self.defense + defense

    def isAlive(self):
        if self.life > 0:
            return True
        else:
            return False
        
    def die(self):
        self.life = 0
        print(self.name, "is dead.")

    def damage(self, enemy):
        return self.strength - enemy.defense
    
    def attack(self, enemy):
        damage = self.damage(enemy)
        enemy.life = enemy.life - damage
        print(self.name, "has done ", damage, " points to ", enemy.name)
        if enemy.isAlive():
            print(enemy.name, "has now: ", enemy.life, " life")
        else:
            enemy.die()

    def getStrength(self):
        return self.strength
    
    def setStrength(self, strength):
        if strength < 0:
            print("Error, has introducido un valor negativo")
        else:
            self.strength = strength

#Creating child class
class Knight(Character):
    #Initializing class + inheriting
    def __init__(self, name ="Default", strength = 20, intelligence = 5, defense = 15, life = 100, sword = 5):
        Character.__init__(self, name, strength, intelligence, defense, life)
        self.sword = sword

    #Adding Sword to inherited checkAttributes
    def checkAttributes(self):
        super().checkAttributes()
        print("-Sword: " , self.sword)

    #Changing sword values
    def changeSword(self):
        weapon = int(input("Choose your weapon: (1) Great Sword, damage 15. (2) Dragon Slayer, damage 20 "))
        if weapon == 1:
            self.sword = 15
        elif weapon == 2:
            self.sword = 20
        else:
            print("Wrong sword number")

    def damage(self, enemy):
        return (self.strength * self.sword) - enemy.defense


#Creating child class
class Mage(Character):
    def __init__(self, name="Default", strength=5, intelligence=20, defense=5, life=100, spellbook = 20):
        super().__init__(name, strength, intelligence, defense, life)
        self.spellbook = spellbook

    #Adding spellbook to inherited checkAttributes
    def checkAttributes(self):
        super().checkAttributes()
        print("-Spellbook: " , self.spellbook)

    def damage(self, enemy):
        return (self.intelligence * self.spellbook) - enemy.defense

#Check if default values are working...
##jhonny = Character()
##jhonny.checkAttributes()

#Check if correct values are working
jhonny = Character("Jhonny", 10, 5, 10)
##jhonny.checkAttributes()

#Leveling up
##jhonny.levelUp(10, 5, 10)
##jhonny.checkAttributes()

#Checking if isAlive
##print("Jhonny is alive: ", jhonny.isAlive())

#Character Dieing
##jhonny.die()
##jhonny.checkAttributes()
##print("Jhonny is alive: ", jhonny.isAlive())

#Create second character to play with
goro = Character("Goro", 50, 1, 100,1000)
##goro.checkAttributes()

#First character attacks second one
##jhonny.attack(goro)
##goro.checkAttributes()


#Using getters and setters
##print(jhonny.getStrength())
##jhonny.setStrength(1000)
##print(jhonny.getStrength())

#Creating a Knight character
pedroTheKnight = Knight("PedroTheKnight")
#Checking attributes with sword
##pedroTheKnight.checkAttributes()
##goro.checkAttributes()

#Check changing Sword feature
##pedroTheKnight.changeSword()
##pedroTheKnight.checkAttributes()
##pedroTheKnight.attack(goro)
##goro.checkAttributes()

#Creating a Mage character
rolfTheMage = Mage("RolfTheMage",5,20,5,100,20)
#rolfTheMage.checkAttributes()
#rolfTheMage.attack(goro)
#goro.checkAttributes()

#Creating a combat simulation
def combat(player1, player2):
    round = 0
    while player1.isAlive() and player2.isAlive():
        print("\nRound ", round)
        player1.attack(player2)
        player2.attack(player1)
        round = round + 1

    if player1.isAlive():
        print(player1.name, " is the winner!")
    elif player2.isAlive():
        print(player2.name, " is the winner!")
    else:
        print("Combat is tied")

combat(rolfTheMage, goro)
#combat(pedroTheKnight, goro)
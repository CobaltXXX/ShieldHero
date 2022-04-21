from item import Item
class Weapon(Item):
    def __init__(self, name, description, id, baseAttackDamage = 0, baseMagicDamage = 0):
        super().__init__(name, description, id)
        self.baseAD = baseAttackDamage
        self.baseMD = baseMagicDamage
        self.currentAD = self.baseAD
        self.currentMD = self.baseMD

    def getBaseAD(self):
        return self.baseAD

    def setBaseAD(self, newBaseAD):
        self.baseAD = newBaseAD

    def getCurrentAD(self):
        return self.currentAD

    def setCurrentAD(self, newCurrentAD):
        self.currentAD = newCurrentAD  

    def getBaseMD(self):
        return self.baseMD

    def setBaseMD(self, newBaseMD):
        self.baseMD = newBaseMD

    def getCurrentMD(self):
        return self.currentMD

    def setCurrentMD(self, newCurrentMD):
        self.currentMD = newCurrentMD 

    def printItemStats(self):
        super().printItemStats() 
        print("Base Attack Damage: " + str(self.baseAD))
        print("Current Attack Damage: " + str(self.currentAD))
        print("Base Magic Damage: " + str(self.baseMD))
        print("Current Magic Damage: " + str(self.currentMD))


#sword = Weapon("Blade", "Standard Blade", 10, 2)
#sword.printItemStats()

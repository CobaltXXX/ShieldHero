from weapon import Weapon

class VassalWeapon(Weapon):
    def __init__(self, name, description, id, baseAttackDamage=0, baseMagicDamage=0, baseSpiritPower = 0):
        super().__init__(name, description, id, baseAttackDamage, baseMagicDamage)
        self.baseSP = baseSpiritPower
        self.currentSP = self.baseSP
        self.inventory = []
        self.inventorySize = 10
        self.strengthMethod = []
        self.heroWeapon = False


    def getBaseSP(self):
        return self.baseSP

    def setBaseSP(self, newBaseSP):
        self.baseSP = newBaseSP
    
    def getCurrentSP(self):
        return self.currentSP

    def setCurrentSP(self, newCurrentSP):
        self.currentSP = newCurrentSP
    
    def getInventory(self):
        return self.inventory

    def getInventorySize(self):
        return self.inventorySize

    def addToInventory(self, item):
        self.inventory.append(item)

    def setInventorySize(self, newInventorySize):
        self.inventorySize = newInventorySize

    def getStrengthMethod(self):
        return self.strengthMethod

    def addStrengthMethod(self, newStrengthMethod):
        self.strengthMethod.append(newStrengthMethod)

    def isHeroWeapon(self):
        return self.heroWeapon

    def printItemStats(self):
        super().printItemStats()
        print("Base Spirit Power: " + str(self.baseSP))
        print("Current Spirit Power: " + str(self.currentSP))
        print("Items in Inventory:")
        for item in self.inventory:
            print(item.getName())
        print("Strengthening Methods:")
        for meth in self.strengthMethod:
            print(self.strengthMethod[meth])
        print("Hero Weapon: " + str(self.heroWeapon))

#scythe = VassalWeapon("Star Scythe", "The weapon of the star hero L'arc from Glass's world", 50, 25, 15)
#scythe.printItemStats()



from ctypes import sizeof
from unicodedata import name


class VassalWeapon:
    def __init__(self, weaponType, wielder, baseDamage = 0, baseMagicDamage = 0, ):
        self.weaponType = weaponType
        self.wielder = wielder
        self.heroWeapon = False
        self.strengthMethod = "None"
        self.inventory = []
        self.inventorySize = 10
        self.baseAD = baseDamage
        self.baseMD = baseMagicDamage
        self.currentAD = 0
        self.currentMD = 0

        
    def getWeaponType(self):
        return self.weaponType 

    def getWielder(self):
        return self.wielder

    def isHeroWeapon(self):
        return self.heroWeapon

    def isHeroWeaponString(self):
        return str(self.heroWeapon)

    def getInventory(self):
        return self.inventory

    def addToInventory(self, item):
        if not(sizeof(self.inventory) <= sizeof(self.inventory) + 1):
            self.inventory.append(item)
        else:
            print("addToInventoryError - Not enough space in inventory - vassalWeapon.py")

    def getInventorySize(self):
        return self.inventorySize

    def setInventorySize(self, newSize):
        self.inventorySize = newSize
        

    def getStrengthMethod(self):
        return self.strengthMethod

    def setStrengthMethod(self, newStrengthMethod):
        self.strengthMethod = newStrengthMethod

    def getBaseAttackDamage(self):
        return self.baseAD

    def setBaseAttackDamage(self, newBaseAD):
        self.baseAD = newBaseAD

    def getBaseMagicDamage(self):
        return self.baseMD

    def setBaseMagicDamage(self, newBaseMD):
        self.baseMD = newBaseMD

    def getCurrentAD(self):
        return self.currentAD

    def setCurrentAD(self, newCurrentAD):
        self.currentAD = newCurrentAD

    def getCurrentMD(self):
        return self.currentMD

    def setCurrentMD(self, newCurrentMD):
        self.currentMD = newCurrentMD

    def printStats(self):
        print("Weapon: " + self.weaponType)
        print("Wielder: " + self.wielder)
        print("Hero Weapon: " + str(self.heroWeapon))
        print("Inventory: " + str(self.inventory))
        print("Inventory Size: " + str(self.inventorySize))
        print("Strengthening Method: " + self.strengthMethod)
        print("Base Attack Damage: " + str(self.baseAD))
        print("Base Magic Damage: " + str(self.baseMD))
        print("Current Attack Damage: " + str(self.currentAD))
        print("Current Magic Damage: " + str(self.currentMD))
        


#myWeapon = VassalWeapon("Sword", "Max")
#myWeapon.printStats()



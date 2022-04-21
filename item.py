class Item:
    def __init__(self, name, description):
        self.name = name
        self.desc = description

        #All boosts are added to stats, therefore default is 0
        #All multipliers are multiplied by the current stat, so the default is 1
        self.invSizeB = 0   #statBoostInventorySize
        self.adB = 0        #statBoostAttackDamage
        self.adM = 1        #statMultiplierAttackDamage
        self.mdB = 0        #statBoostMagicDamage
        self.mdM = 1        #statMultiplierMagicDamage
        self.spB = 0        #statBoostSpiritPower
        self.spM = 1        #statMultiplierSpiritPower
        self.mpB = 0        #statBoostMagicPower
        self.mpM = 1        #statMultiplierMagicPower
        self.hpB = 0        #statBoostHP
        self.hpM = 1        #statMultiplierHP
        self.strengthB = 0  #statBoostStrength
        self.strengthM = 1  #statMultiplierStrength
        self.defB = 0       #statBoostDefense
        self.defM = 1       #statMultiplierDefense

        self.slot = 0  #no slots is default = 0
        self.slotOverrides = [] #list of integers

    def getName(self):
        return self.name

    def getDescription(self):
        return self.desc

    def setDescription(self, newDesc):
        self.desc = newDesc

    def getStatBoostInventorySize(self):
        return self.invSizeB

    def setStatBoostInventorySize(self, newBoost):
        self.invSizeB = newBoost

    def getStatBoostAD(self):
        return self.adB

    def setStatBoostAD(self, newBoost):
        self.adB = newBoost

    def getStatMultAD(self):
        return self.adM

    def setStatMultAD(self, newMult):
        self.adM = newMult

    def getStatBoostMD(self):
        return self.mdB

    def setStatBoostMD(self, newBoost):
        self.mdB = newBoost
        
    def getStatMultMD(self):
        return self.mdM

    def setStatMultMD(self, newMult):
        self.mdM = newMult

    def getStatBoostSP(self):
        return self.spB

    def setStatBoostSP(self, newBoost):
        self.spB = newBoost

    def getStatMultSP(self):
        return self.spM

    def setStatMultSP(self, newMult):
        self.spM = newMult

    def getStatBoostMP(self):
        return self.mpB

    def setStatBoostMP(self, newBoost):
        self.mpB = newBoost

    def getStatMultMP(self):
        return self.mpM

    def setStatMultMP(self, newMult):
        self.mpM = newMult

    def getStatBoostHP(self):
        return self.hpB

    def setStatBoostHP(self, newBoost):
        self.hpB = newBoost

    def getStatMultHP(self):
        return self.hpM

    def setStatMultHP(self, newMult):
        self.hpM = newMult

    def getStatBoostStrength(self):
        return self.strengthB

    def setStatBoostStrength(self, newBoost):
        self.strengthB = newBoost

    def getStatMultStrength(self):
        return self.strengthM

    def setStatMultStrength(self, newMult):
        self.strengthM = newMult

    def getStatBoostDefense(self):
        return self.defB

    def setStatBoostDefense(self, newBoost):
        self.defB = newBoost

    def getStatMultDefense(self):
        return self.defM

    def setStatMultDefense(self, newMult):
        self.defM = newMult

    def getSlot(self):
        return self.slot
    
    def setSlot(self, newSlot):
        self.slot = newSlot

    def getOverrideSlots(self):
        return self.slotOverrides

    def setOverrideSlots(self, newSlots):
        self.slotOverrides = newSlots

    def printItemStats(self):
        print("Item: " + self.name)
        print("Description: " + self.desc)
        print("Item slot: " + str(self.slot))
        print("Stats:\n")
        print("Inventory Size: +" + str(self.invSizeB))
        print("Attack Damage +" + str(self.adB) + " x" + str(self.adM))
        print("Magic Damage +" + str(self.mdB) + " x" + str(self.mdM))
        print("Spirit Power +" + str(self.spB) + " x" + str(self.spM))
        print("Magic Power +" + str(self.mpB) + " x" + str(self.mpM))
        print("Health Points +" + str(self.hpB) + " x" + str(self.hpM))
        print("Strength +" + str(self.strengthB) + " x" + str(self.strengthM))
        print("Defense +" + str(self.defB) + " x" + str(self.defM))

#standardArmor = Item("Armor", "secret aromor\n bruh momento")
#standardArmor.setSlot(4)
#standardArmor.setStatBoostDefense(15)
#standardArmor.setStatBoostStrength(-2)
#standardArmor.printItemStats()

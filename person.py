class Person:
    def __init__(self, name, baseMP = 0, baseHP = 10, baseStrength = 10, baseDefense = 10, lvl=1):
        self.name = name
        self.baseMP = baseMP
        self.netMP = 0
        self.baseHP = baseHP
        self.currentHP = 0
        self.totalHP = 10
        self.baseStrength = baseStrength
        self.netStrength = 0
        self.baseDefense = baseDefense
        self.netDefense = 0
        self.lvl = lvl
        
        self.equip1 = None    #head
        self.equip2 = None    #face
        self.equip3 = None    #chestUnder
        self.equip4 = None    #chestOver
        self.equip5 = None    #shoulderRight
        self.equip6 = None    #shoulderLeft
        self.equip7 = None    #wristRight
        self.equip8 = None    #wristLeft
        self.equip9 = None    #handRight
        self.equip10 = None   #handLeft
        self.equip11 = None   #palmRight
        self.equip12 = None   #palmLeft
        self.equip13 = None   #legsUnder
        self.equip14 = None   #legsOver
        self.equip15 = None   #feet
        self.equip16 = None   #waist
        self.equip17 = None   #neck
        self.equip18 = None   #earRight
        self.equip19 = None   #earLeft

        
    def getName(self):
        return self.name
    
    def setName(self, newName):
        self.name = newName

    def getBaseMagicPower(self):
        return self.baseMP

    def setBaseMagicPower(self, newBaseMP):
        self.baseMP = newBaseMP

    def getNetMagicPower(self):
        return self.netMP

    def setNetMagicPower(self, newNetMP):
        self.netMP = newNetMP

    def getBaseHP(self):
        return self.baseHP

    def setBaseHP(self, newBaseHP):
        self.baseHP = newBaseHP

    def getCurrentHP(self):
        return self.currentHP

    def setCurrentHP(self, newCurrentHP):
        self.currentHP = newCurrentHP

    def getTotalHP(self):
        return self.totalHP

    def setTotalHP(self, newTotalHP):
        self.totalHP = newTotalHP

    def getBaseStrength(self):
        return self.baseStrength

    def setBaseStrength(self, newBaseStrength):
        self.baseStrength = newBaseStrength

    def getNetStrength(self):
        return self.netStrength

    def setNetStrength(self, newNetStrength):
        self.netStrength = newNetStrength

    def getBaseDefense(self):
        return self.baseDefense

    def setBaseDefense(self, newBaseDefense):
        self.baseDefense = newBaseDefense

    def getNetDefense(self):
        return self.netDefense

    def setNetDefense(self, newNetDefense):
        self.netDefense = newNetDefense

    def getLevel(self):
        return self.lvl
    
    def setLevel(self, newlvl):
        self.lvl = newlvl
    

    def equipItem(self, item, slot):
        if slot == 1:
            self.equip1 = item
        elif slot == 2:
            self.equip2 = item
        elif slot == 3:
            self.equip3 = item
        elif slot == 4:
            self.equip4 = item
        elif slot == 5:
            self.equip5 = item
        elif slot == 6:
            self.equip6 = item
        elif slot == 7:
            self.equip7 = item
        elif slot == 8:
            self.equip8 = item
        elif slot == 9:
            self.equip9 = item
        elif slot == 10:
            self.equip10 = item
        elif slot == 11:
            self.equip11 = item
        elif slot == 12:
            self.equip12 = item
        elif slot == 13:
            self.equip13 = item
        elif slot == 14:
            self.equip14 = item
        elif slot == 15:
            self.equip15 = item
        elif slot == 16:
            self.equip16 = item
        elif slot == 17:
            self.equip17 = item
        elif slot == 18:
            self.equip18 = item
        elif slot == 19:
            self.equip19 = item
        else:
            print("equipItemFailiure - Non-valid Equip Slot - person.py")
    

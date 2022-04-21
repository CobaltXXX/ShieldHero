class Item:
    def __init__(self, name, description, id):
        self.name = name
        self.desc = description
        self.id = id

    def getName(self):
        return self.name

    def getDescription(self):
        return self.desc

    def setDescription(self, newDesc):
        self.desc = newDesc

    def getID(self):
        return self.id

    def setID(self, newID):
        self.id = newID

    def printItemStats(self):
        print("Item: " + self.name)
        print("Description: " + self.desc)
        print("ID Number: " + str(self.id))
       

#standardArmor = Item("Armor", "secret aromor\n bruh momento")
#standardArmor.printItemStats()

from xml.etree.ElementTree import tostring
from vassalWeapon import VassalWeapon
from person import Person
from item import Item

class LegendaryWeapon(VassalWeapon):
    def __init__(self, weaponType, wielder, totalSP):
        super().__init__(weaponType, wielder)
        self.totalSP = totalSP
        self.heroWeapon = True

    def getTotalSP(self):
        return self.totalSP

    def setTotalSP(self, newTotalSP):
        self.totalSP = newTotalSP

    def printStats(self):
        super().printStats()
        print("Total SP: " + str(self.totalSP))
        
me = Person("Max", 100, 10501050, 3, 15, 100)
myWeapon = LegendaryWeapon("Sword", me, 1000)
myWeapon.printStats()

    
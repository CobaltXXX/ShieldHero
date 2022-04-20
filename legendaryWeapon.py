from xml.etree.ElementTree import tostring
from sqlalchemy import true
from vassalWeapon import VassalWeapon

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
        
#myWeapon = LegendaryWeapon("Sword", "Max", 1000)
#myWeapon.printStats()

    
from xml.etree.ElementTree import tostring
from vassalWeapon import VassalWeapon


class LegendaryWeapon(VassalWeapon):
    def __init__(self, name, description, id, baseAttackDamage=0, baseMagicDamage=0, baseSpiritPower=0):
        super().__init__(name, description, id, baseAttackDamage, baseMagicDamage, baseSpiritPower)
        self.heroWeapon = True

#sword = LegendaryWeapon("Legendary Sword", "The sword of Ren, the sword hero in Raphtalia's world", 10010001, 100, 15, 75)
#sword.printItemStats()

    
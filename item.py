class Item:
    def __init__(self, name, description, string15, slots):
        self.name = name
        self.desc = description

        split15 = string15.split(",")
        stat15 = []
        i = 1
        for s in split15:
            if i < 16:
                stat15[i] = int(s)
                i += 1

        self.invSizeB = stat15[1]   #statBoostInventorySize
        self.adB = stat15[2]        #statBoostAttackDamage
        self.adM = stat15[3]        #statMultiplierAttackDamage
        self.mdB = stat15[4]        #statBoostMagicDamage
        self.mdM = stat15[5]        #statMultiplierMagicDamage
        self.spB = stat15[6]        #statBoostSpiritPower
        self.spM = stat15[7]        #statMultiplierSpiritPower
        self.mpB = stat15[8]        #statBoostMagicPower
        self.mpM = stat15[9]        #statMultiplierMagicPower
        self.hpB = stat15[10]       #statBoostHP
        self.hpM = stat15[11]       #statMultiplierHP
        self.strengthB = stat15[12] #statBoostStrength
        self.strengthM = stat15[13] #statMultiplierStrength
        self.defB = stat15[14]      #statBoostDefense
        self.defM = stat15[15]      #statMultiplierDefense

        slotSplit = slots.split(",")
        for slot in slotSplit:
            slotSplit[slot] = int(slot)
greycard = 60


def ratio(num1, num2, num3, num4):
    if (num4 == 0):
        num4 = 1
    ratio = float((num1 * num2 * (2 - num3)) / (num4))
    return str(round(ratio, 2))


class ThreeStar:
    name = ""
    currentlvl = 1
    exp = 0
    leftoverexp = 0
    get1lvl = 40
    maxexp = 5220
    maxlvl = 30
    sacrificeexp = 100

    def __init__(self, name, curlvl, curexp):
        self.name = name
        self.currentlvl = curlvl
        self.exp = curexp

    def maxedOut(self):
        if (self.currentlvl == self.maxlvl):
            return False
        else:
            return True

    def increaseLvl(self, expp):
        lvlexp = expp + self.leftoverexp
        # print " --- Exp Gained: " + str(expp) + " | Left over: " + str(self.leftoverexp) + " --- "
        # print "lvlexp = " + str(lvlexp)
        # print " --- " + str(self.get1lvl) + " --- "
        # print lvlexp >= self.get1lvl
        if ((lvlexp >= self.get1lvl) & (self.exp < self.maxexp)):
            # print "You leveled up!"
            self.currentlvl += 1
            self.leftoverexp = lvlexp - self.get1lvl
            self.increaseCap()
        else:
            self.leftoverexp += expp
            # print "New leftover exp = " + str(self.leftoverexp)

        if (self.leftoverexp >= self.get1lvl):
            self.increaseLvl(0)
            #print "Levelin' Again"

    def increaseCap(self):
        self.get1lvl += 10

    def absorb(self, card):
        if (self.exp + card < self.maxexp):
            self.exp += card  # Current Experience of Card
            expgained = card  # How much exp you're gaining
            self.increaseLvl(expgained)
        else:
            self.currentlvl = 30
            self.exp = self.maxexp
            print "Card is maxed out."
            self.info()
        return 0

    def info(self):
        print "\nCard Name: " + self.name
        print "Lvl " + str(self.currentlvl) + " |-----| " + \
            str(self.leftoverexp) + "/" + str(self.get1lvl)
        print "Current Exp: " + str(self.exp)
        print "Exp needed to reach max level: " + str(self.maxexp - self.exp)
        print "This card is worth " + \
            str((self.sacrificeexp*self.currentlvl)*(2-(self.maxedOut()))) + \
            "exp"
        print "If you fed " + str(self.exp/greycard) + \
            " grey cards into your main card, you'd only gain " + \
            str(self.exp) + "exp. (Ratio = " + \
            ratio(float(self.sacrificeexp), self.currentlvl,
                  self.maxedOut(), self.exp) + \
            ")"

card = ThreeStar("Sasuke", 1, 0)

while (card.currentlvl < card.maxlvl):
    print card.info()
    card.absorb(greycard)

###############
# Program 11.6 #
#################
# Known Problems #
# -if an invalid input is given, it can't be handled and you get an error. Too much time needed to fix this, but it works as designed technically

from os import system as sys
import random, time

print "Welcome to GardenSim!\n" + "________________________\n" + "It may initially appear long and potentially sophisticated\n" + "It's actually very disappointing and not really efficient\n(hmm, familiar..)\n"
raw_input("[Enter]")
print "So here's a gardening 'sandbox' 'game'"
time.sleep(2)
sys('cls')


class Player:
    def __init__(self, name):
        self.name = name
        self.response = {}
        self.gameTime = 0
        self.rateTime = 1
        self.balance = 0
        self.gardens = []

    def __str__(self):
        return self.name

    def standby(self):
        for moves in range(5, 0, -1):  # this affects how many actions the player can perform in a day
            ans = ""
            sys('cls')
            space = 8
            ind = " " * space
            userTxt = ("User: " + self.name)
            print (" " * space) + "GardenSim" + (" " * space)
            print ("_" * (13 - (len(userTxt) // 2))) + userTxt + ("_" * (13 - (len(userTxt) // 2)))  # Possible Inputs\/
            print "Actions:\n" + ind + "View Gardens: [v,V]\n" + ind + "New Garden: [+g,+G]\n" + ind + "New Plant: [+p,+P]\n" + ind + "Move Plant: [m,M]\n" + ind + "End Day: [Enter]"
            print "(Energy:" + str(moves) + ", Days:" + str(self.gameTime) + ")"
            ans = str(raw_input()).upper()
            sys('cls')
            if ans == "":
                return
            elif ans == "+G":
                self.newGarden()
            elif ans == "+P":
                self.newPlant()
            elif ans == "V":
                self.viewGardens()  # viewing gardens uses energy because old people spend 10 minutes looking over their lillies and just nap for the rest of the day
            elif ans == "M":
                self.movePlant()
            else:
                moves += 1

    def newGarden(self):
        if len(self.gardens) > 0:
            last = self.gardens[-1].size
        else:
            last = 1

        sys('cls')
        print "\nName your garden?"
        ans = raw_input("[y,n]").upper()
        if ans == "Y":
            sys('cls')
            print "What would you like to name your garden?"
            name = str(raw_input())
            self.gardens.append(Garden(name, self, random.randint(last, last + 3)))
        else:
            self.gardens.append(Garden((self.name + "'s garden"), self, random.randint(last, last + 3)))

        sys('cls')
        print "You've started a new garden!"
        print "(added: " + str(self.gardens[-1].name) + ", size:" + str(self.gardens[-1].size) + ")"
        raw_input("[Neat!]")
        sys('cls')

    def timepass(self):
        self.gameTime += self.rateTime
        for gar in range(len(self.gardens)):
            for plnt in range(len(self.gardens[gar].flowers)):
                self.gardens[gar].flowers[plnt].height += self.rateTime
                self.balance += self.gardens[gar].flowers[plnt].height
        print "The day passes..."
        print "(Time:" + str(self.gameTime) + ")"

        frame = ["zzz", "Zzz", "zZz", "zzZ"]
        for i in range(20):
            sys('cls')
            print "The day passes..."
            print frame[i % 4]
            # print ("_"*(i%6))+"."+("_"*(6-(i%6)))
            time.sleep(0.05)
        if self.gameTime >= 3:
            print "Congrats, you've been playing this for too long"
        raw_input("[Enter]")
        self.rateTime = 1

    def newPlant(self):
        sys('cls')
        if len(self.gardens) > 0:
            print "Where would you like to plant?"
            for i in range(len(self.gardens)):
                if len(self.gardens[i].flowers) < self.gardens[i].size:
                    print str(i + 1) + ".) size=" + str(self.gardens[i].size) + " : flowers" + str(
                        self.gardens[i].flowers)
                else:
                    print str(i + 1) + ".) Full"
            ans = int(raw_input()) - 1
            sys('cls')
            print "Creating Flower..."
            self.gardens[ans].addflower(
                Flower(raw_input("Plant Name="), 1, raw_input("Color="), raw_input("Type of petal=")))
            sys('cls')
            print "Planted! (" + str(self.gardens[ans].flowers[-1]) + ")"
            raw_input("[neat]")
        else:
            print "You have no gardens!"
            raw_input("[Oh]")

    def viewGardens(self):
        if len(self.gardens) > 0:
            print "Enter a garden number to see it's plants\n" + "Press Enter to exit garden viewer\n"
            print "___--=Gardens=--___"
            for i in range(len(self.gardens)):
                print str(i + 1) + ". '" + self.gardens[i].name + "' ) size:" + str(
                    self.gardens[i].size) + ", flowers:" + str(len(self.gardens[i].flowers))
            ans = raw_input("[Enter]")
            sys('cls')
            if ans == "":
                return
            else:
                self.gardens[int(ans) - 1].view()

        else:
            print "\nYou have no gardens!\n"
            print "Start a new one?"
            ans = (raw_input('[y,n]')).upper()
            if ans == "Y":
                self.newGarden()

            else:
                sys('cls')
                return

    def movePlant(self):
        sys('cls')
        print "Where would you like move from?"
        for i in range(len(self.gardens)):
            print str(i + 1) + ".) size:" + str(self.gardens[i].size) + " | flowers:" + str(
                len(self.gardens[i].flowers))
        ans = int(raw_input("Old Garden:")) - 1, int(raw_input("Flower:")) - 1, int(raw_input("New Garden:")) - 1
        flw = self.gardens[ans[0]].flowers[ans[1]]
        self.gardens[ans[2]].flowers.append(flw)
        self.gardens[ans[0]].flowers.remove(flw)
        sys('cls')
        print self.gardens[ans[2]]
        print flw
        print "Successfully moved!"
        raw_input("[neat]")


class Flower:
    def __init__(self, flower, height, color, petal):
        self.flower = flower
        self.height = height
        self.color = color
        self.petal = petal

    def __str__(self):
        return str(self.flower) + " | Height: " + str(self.height) + " in. | Color: " + str(
            self.color) + " | Petal: " + str(self.petal)

    def plant(self, aGarden):
        if (self not in aGarden.flowers) and (aGarden.size > len(aGarden.flowers)):
            aGarden.flowers.append(self)
            self.garden = aGarden
            print str(self.flower) + " successfully planted!"
        else:
            print "This " + self.flower + " is already in this garden!"
            print "Dig up?"
            ans = raw_input("[Y/N]")
            if ans in ['y', 'Y']:
                aGarden.flowers.remove(self)
                self.garden = None
                print self.flower + " has been dug up!"
                print "You may replant this " + self.flower + " at any time"
                raw_input("[neat]")
            sys('cls')

    def move(self, bGarden):
        if bGarden.size > len(bGarden.flowers):
            bGarden.flowers.append(self)
            self.garden.flowers.remove(self)
        else:
            print "This " + str(self.flower) + " cannot be moved at this time"
            raw_input("[Okay]")


class Garden:
    def __init__(self, name, owner, size):
        self.name = name
        self.owner = owner
        self.size = size
        self.flowers = []

    def __str__(self):
        return str(self.name) + "(size:" + str(self.size) + "): " + str(len(self.flowers))

    def addflower(self, flower):
        if self.size > len(self.flowers):
            self.flowers.append(flower)
        else:
            print "This garden is full!"
            raw_input("[Okay]")

    def showplants(self):
        list = []
        for i in range(len(self.flowers)):
            list.append(self.flowers[i].flower)
        return list

    def view(self):
        print self.name
        print "_" * len(self.name)
        for flwr in range(len(self.flowers)):
            print self.flowers[flwr]
        print "([Enter]:Exit | [+p]:Add Plant)"
        raw_input("[neat]")
        sys('cls')


user = ""
while user == "":
    sys('cls')
    print "\nWhat would you like your name to be?\n"
    user = str(raw_input())
    sys('cls')
    print "\nYou entered " + user + ".\nIs that okay?\n"
    ans = str(raw_input("[y/n]")).upper()
    if ans == "N":
        user = ""
    elif ans == "Y":
        user = Player(user)
    else:
        user = ""

# Player(raw_input("Name:"))

frame = ["oooo", "Oooo", "oOoo", "ooOo", "oooO", "oooo"]
for i in range(20):
    sys('cls')
    print "Welcome to GardenSim, " + user.name + "!"
    print frame[i % len(frame)]
    time.sleep(0.05)
while True:
    user.standby()
    user.timepass()
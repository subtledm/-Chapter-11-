###############
# Program 11.6 #
#################
from os import system as sys
import turtle
from random import randint
# Pizza Sim #
#keep track of pizzas, don't let them fall out of the oven (each turn,pizzas go through the oven a percentage)
#open orders to see pending orders
#if it's a buffet day (random per game), remember to put buffet pizzas in the oven. If a buffet pizza is a turn late, mgr will yell
#don't run out of toppings, send workers to go get toppings, but be careful not to decrease production time and get behind
#workers have a random chance to get distracted for a turn
#class specifically for pizza creation
#remakes will deduct points or whatever
#make a list of active pizzas that automatically "next"'s each of them
#adding toppings will be a typing game. The ticket will be displayed, and each topping will print in order and the player will be required to get every topping spelled correctly or you'll love money and get a strike
#price will be calculated when taking orders, otherwise the price will be automatically forwarded to ticket

#class topping:
#    def __init__(self):
#        self.mt = turtle.Turtle()
#        self.mt.ht()
#        self.mt.pu()
#    def crust(self,type,size): #size=str(s,m,l)
#
#    def sauce(self,type,amount):
#
#    def cheese(self,type,amount): #type=str amount=str(light,reg,xtra)
#
#    def toppings(self,topping): #topping=list

class Manager:
    def __init__(self):
        self.name = ["Joe","Josh","Deon","Shauna"][randint(0,3)]
        self.balance = 0
        self.pastorders = []

    def deposit(self,order,amount):
        self.balance += amount
        self.pastorders.append((order,amount))
mngr = Manager()
class Pizza:
    def __init__(self,size,crust,sauce,cheese,toppings):
        self.eta = 10
        self.size = size
        self.crust = crust
        self.sauce = sauce
        self.cheese = cheese
        self.toppings = toppings
        self.order = (size,crust,sauce,cheese,toppings)
        self.price = self.calcPrice()
    def __str__(self):
        return "The "+self.toppings+" is at "+self.phases[self.phase][0]+" right now"
    def calcPrice(self):
        sizeP = {'large':10,'medium':8,'small':6}
        crustP = {'handtossed':0,'thin':0,'pan':1,'stuffed':2}
        cheeseP = {'light':1,'regular':1,'extra':1.5}
        sauceP = 0
        toppings = 1
        prices = [sizeP,crustP,0,cheeseP,self.order[4]]
        self.tPrice = 0
        for fac in range(len(self.order)):
            self.tPrice += int(prices[fac][str(self.order[fac])]) #left off here
        #price = 1.07*(sizeP[self.order[0]]+crustP[self.order[1]])
        print order
        print tPrice
        raw_input()
        return tPrice
    def nextTurn(self,rate):
        if self.eta > 0:
            self.eta -= rate
        else:
            print "Order Up!"
            mngr.deposit(self.order,self.price)

    #    if self.phases[self.phase][1] <= 0:
    #        if len(self.phases) == self.phase:
    #            print "Order Up!"
    #            self.phase = "Done"
    #            mngr.deposit(order,27.33)
    #        else:
    #            self.phase += 1
    #    else:
    def checkup(self):
        return "That's going to take about "+str(self.phase)+" more minute(s)"

largepep = Pizza('large','pan','classic','regular',('pepperoni'))
for i in range(10):
    largepep.nextTurn(1)
    print largepep
    raw_input("[Next]")
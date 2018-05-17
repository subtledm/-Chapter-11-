###############
# Program 11.5 #
#################
from os import system as sys
from random import randint
import turtle, math

class Graph:
    def __init__(self,lines):
        self.turtle = turtle.Turtle()
        self.turtle.pu()
        self.turtle.ht()
        self.maxunit = 0
        for i in range(len(lines)):
            if abs(lines[i].yInt) > abs(self.maxunit):
                self.maxunit = abs(lines[i].yInt)

    def Draw(self,start,end):
        self.turtle.goto(start)
        self.turtle.pd()
        self.turtle.goto(end)
        self.turtle.pu()

    def border(self):
        direc = (200,200,400,400,400,200)
        self.turtle.speed(0)
        self.turtle.pensize('5')
        self.turtle.pencolor('black')
        for i in range(len(direc)):
            self.turtle.forward(direc[i])
            self.turtle.right(90)
            if i==0:
                self.turtle.pd()
        self.turtle.pu()

    def axis(self):
        self.turtle.pensize(2)
        self.turtle.color('grey')
        for y in range(self.maxunit * -1, self.maxunit + 1):
            self.turtle.goto(10, (200/self.maxunit) * y)
            self.turtle.pd()
            self.turtle.goto(-10, (200/self.maxunit) * y)
            self.turtle.pu()
        for x in range(self.maxunit*-1,self.maxunit+1):
            self.turtle.goto((200/self.maxunit)*x,10)
            self.turtle.pd()
            self.turtle.goto((200/self.maxunit)*x,-10)
            self.turtle.pu()


class Line:
    def __init__(self, slope, yInt):
        self.slope = slope
        self.yInt = yInt

    def __str__(self):
        return "Line: slope=(" + str(self.slope) + ") | y-Intercept=(" + str(self.yInt) + ")"

    def isParallel(self, second):
        if self.slope == second.slope:
            return True
        else:
            return False

    def isPerpendicular(self, second):
        if self.slope == ((second.slope) * -1):
            return True
        else:
            return False

    def intersectsAt(self, second):
        x = (self.yInt - second.yInt) / (second.slope - self.slope)
        return x, (self.slope * x) + self.yInt

    def plot(self):
        global tilly
        # tilly.goto(-200,self.yInt+(self.slope*200))
        # tilly.goto(0,self.yInt)
        tilly.turtle.pu()
        tilly.turtle.ht()


        tilly.turtle.goto(-200, ((self.slope * -200) + self.yInt * (200/tilly.maxunit)))
        tilly.turtle.setheading(tilly.turtle.towards(0,self.yInt * (200/tilly.maxunit)))
        tilly.turtle.forward(-10)
        print "Drawing| m=" + str(self.slope) + " , b=" + str(self.yInt)

        while ((tilly.turtle.ycor()>200)or(tilly.turtle.ycor()<-200)):
            tilly.turtle.forward(1)
        tilly.turtle.pd()
        while tilly.turtle.xcor()<200 and tilly.turtle.ycor()<200 and tilly.turtle.ycor()>-200:
            tilly.turtle.forward(1)
        tilly.turtle.pu()


sys('cls')
# lines = [Line(2,3),Line(-0.5,7)]
lines = []
rRange = 3
for i in range(10):
    lines.append(Line(randint(rRange * -1, rRange), randint(rRange * -1, rRange)))
# lines[0].plot()
# raw_input("[Enter:Restart]")
#maxunit = 0
#for i in range(len(lines)):
#    if abs(lines[i].yInt) > abs(maxunit):
#        maxunit = abs(lines[i].yInt)


#tillyini()
tilly = Graph(lines)
tilly.border()
tilly.axis()
color = ['red','orange','#f4ee42','green','blue','purple']
tilly.turtle.pensize(2)
tilly.turtle.speed(4)
for i in range(len(lines)):
    tilly.turtle.pencolor(color[i%len(color)])
    lines[i].plot()

sys('cls')
print "Done"
raw_input()
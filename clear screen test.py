from os import system as sys

class c:
    def pause(self):
        raw_input("[...]")
        sys('cls')
    def lr(self):
        sys('cls')

    def msg(self,text):
        raw_input(text)
        sys('cls')

Clear = c.lr()

print "Here's the bee movie scrip"
clear
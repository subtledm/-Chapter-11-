from os import system as sys
import cImage as image
imgList = ["Spirograph.jpg","hawdawn1.jpg"]

class dog:
    def __init__(self,name):
        self.name = name

    def invert(self,img,x,y):
        pix = img.getPixel(x, y)
        newR = 255 - pix.getRed()
        newG = 255 - pix.getGreen()
        newB = 255 - pix.getBlue()
        return newR,newG,newB
def load(img):
    img = image.Image(img)
    iDim = img.getWidth(), img.getHeight()
    newimg = image.EmptyImage(iDim[0],iDim[1])

    win = image.ImageWin(iDim[0], iDim[1])

    # newimg.setDelay(0) #no animation
    # newimg.setDelay(1,100) #animated
    print "Loading..."
    for y in range(iDim[1]):
        for x in range(iDim[0]):
            #pix = img.getPixel(x, y)

            # try calling a function here to change the rgb values
            # maybe call function from image.Pixel


            newb = Filter.invert(img,x,y)
            newpixel = image.Pixel(newb[0],newb[1],newb[2])
            newimg.setPixel(x, y, newpixel)
        newimg.draw(win) #remove this for no animation, chrome sees it as frozen (is not)
    sys('cls')
    newimg.draw(win)
    win.exitonclick()

Filter = dog('Jake')
while True:
    load(imgList[1])
    raw_input("[Done]")

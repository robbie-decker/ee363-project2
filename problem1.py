from cImage import *
import os
# from Tkinter import *

def removeRedEyes(imageFileName, col1, row1, col2, row2):
    win = ImageWin("redEyesRemoval", 800, 500)  # redEyes1.gif is 395x489
    oldImage = FileImage(imageFileName)
    oldImage.draw(win)

    newImage = EmptyImage(oldImage.getWidth(), oldImage.getHeight())
    for row in range(newImage.getHeight()):
        for col in range(newImage.getWidth()):
            v = oldImage.getPixel(col, row)
            if (row1<row<row2 and v.red>150 and v.blue+v.green<v.red ) and (col1<col<col2 and v.red>150 and v.blue+v.green<v.red):
                v.red = (v.blue + v.green) // 2
            newImage.setPixel(col, row, v)
    newImage.setPosition(newImage.getWidth() + 1, 0)
    newImage.draw(win)
    print(win.getMouse())
    print(win.getMouse())
    win.exitOnClick()

if __name__ == '__main__':
    removeRedEyes("redEyes1.gif",85,180,261,222)
    removeRedEyes("redEyes2.gif",85,180,261,222)
    removeRedEyes("redEyes1.gif",85,180,261,222)
    
    # here = os.path.dirname(os.path.abspath(__file__))
    # print(here)
    # FileImage("redEyes1.gif")

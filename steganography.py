from cImage import FileImage, ImageWin
import base64
import os
# from Tkinter import *
col1 = 10
col2 = 20
row1 = 250
row2 = 300


# Below is where we will be changing the color chanels
# This searches in the sky of the img which is a uniform blue
# (10, 250)
# (20, 300)

def stegano(imageFileName, secret):
    binary = " ".join(['{0:08b}'.format(x)for x in bytes(secret, "ascii")])
    bin_array = binary.split(" ")

    image = FileImage(imageFileName)
    win = ImageWin("Encoded Window", image.getWidth(), image.getHeight())

    for row in range(row1, row2):
        for col in range(col1, col2):
            v = image.getPixel(col, row)
            print(v, "before")              
            # v.red = v.red & 0b11110000
            # v.green = v.green & 0b11110000
            # v.blue = v.blue & 0b11110000
            v.red = 0
            v.green = 0
            v.blue = 0

            print(v, "after")

            image.setPixel(col, row, v)

    image.draw(win)

    print(win.getMouse())
    print(win.getMouse())
    win.exitOnClick()



def reverseStegano(imageFileName):
    pass

def test():
    x = int('01110100', 2)
    y = 240
    test = "test sentence"
    test_bytes = bytes(test, "ascii")
    encode = " ".join(['{0:08b}'.format(x)for x in test_bytes])
    print(test_bytes)
    # encode = " ".join('{0:08b}'.format(ord(x), 'b')for x in test)
    # encode = " ".join(format(x,'b')for x in bytearray(test, 'utf-8'))
    
    # binary_int = int("11000010110001001100011", 2)
    # byte_number = binary_int.bit_length() + 7 // 8
    # binary_array = binary_int.to_bytes(byte_number, "big")
    # ascii_text = binary_array.decode()
    # print(ascii_text)
    
    print(map(bin,bytearray(test, 'utf8')))
    print(chr(x))
    print(chr(y))
    bin_array = encode.split(" ")
    print(encode)
    for x in bin_array:
        print(x.strip())
    # print(decode)
    # print(outcome, "what we added")
    # print(int('11111111', 2), "what we want")

if __name__ == '__main__':
    # test()

    stegano("nyc.gif", "shh its is a secret")
    # stegano("nyc_night.gif", "shh its is a secret")

    
    # here = os.path.dirname(os.path.abspath(__file__))
    # print(here)
    # FileImage("redEyes1.gif")

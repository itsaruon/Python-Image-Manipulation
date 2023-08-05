from cImage import *

greenColor = Pixel(0,255,0)
redColor = Pixel(255,0,0)

platform = EmptyImage(300,300)
Lab12 = ImageWin("Lab 12",300,300)

for m in range (300):
    platform.setPixel(150,m,greenColor)
for m in range (150,300):
    platform.setPixel(m,m,redColor)
for m in range (300):
    platform.setPixel(m,150,greenColor)

platform.draw(Lab12)
platform.save("Lab12.gif")
Lab12.exitonClick()

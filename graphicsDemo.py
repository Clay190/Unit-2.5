#Clay Kynor
#9/20/17
#graphicsDemo.py - Intro to ggame

from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
magenta = Color(0xFF00FF,1)

blackOutline = LineStyle(5,black) #pixels, color
blueOutline = LineStyle(5,blue) #pixels, color

redRectangle = RectangleAsset(300,200,blackOutline,magenta) #width, height, outline, fill
blueCircle = CircleAsset(100,blueOutline,green)

Sprite(redRectangle)
Sprite(blueCircle,(150,100))
App().run()












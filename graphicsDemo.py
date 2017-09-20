#Clay Kynor
#9/20/17
#graphicsDemo.py - Intro to ggame

from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,0.2)
black = Color(0x000000,1)
magenta = Color(0xFF00FF,1)
gray = Color(808080,1)

blackOutline = LineStyle(3,black) #pixels, color
blueOutline = LineStyle(3,blue) #pixels, color

redRectangle = RectangleAsset(300,200,blackOutline,magenta) #width, height, outline, fill
blueCircle = CircleAsset(100,blackOutline,green)
greenEllipse = EllipseAsset(50,20,blackOutline,red)
blackLine = LineAsset(120,100,blackOutline)
redTriangle = PolygonAsset([(150,0),(0,200),(300,200)], blueOutline,blue)
text = TextAsset("Clay", fill=gray,style="bold 20pt Times")

Sprite(blackLine)
Sprite(redRectangle)
Sprite(blueCircle,(150,100))
Sprite(greenEllipse,(150,100))
Sprite(redTriangle)
Sprite(text,(125,83))
App().run()












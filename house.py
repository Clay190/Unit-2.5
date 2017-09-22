#Clay Kynor
#9/20/17
#house.py - house picture

from ggame import *

brown = Color(0x8B540F,1)
blueLight = Color(0x1E90FF,0.5)
black = Color(0x000000,1)
darkBrown = Color(0x644628,1)
pink = Color(0xAA3FAE,1)

blackOutline = LineStyle(2,black)

brownTriangle = PolygonAsset([(250,0),(0,200),(500,200)],blackOutline,brown)
blueWindow = RectangleAsset(50,80,blackOutline,blueLight)
wall = RectangleAsset(400,300,blackOutline,darkBrown)

Sprite(wall, (50,200))
Sprite(brownTriangle)
Sprite(blueWindow,(300,300))
App().run()
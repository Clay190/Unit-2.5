#Clay Kynor
#9/20/17
#house.py - house picture

from ggame import *

brown = Color(0x8B540F,1)
blueLight = Color(0x0080FF,1)
black = Color(0x000000,1)
darkBrown = Color(0x644628,1)
pink = Color(0xAA3FAE,1)

blackOutline = LineStyle(2,black)

brownTriangle = PolygonAsset([(250,0),(0,200),(500,200)],blackOutline,brown)
pinkDoor = RectangleAsset(90,150,blackOutline,pink)
blueWindow = EllipseAsset(50,50,blackOutline,blueLight)
wall = RectangleAsset(400,300,blackOutline,darkBrown)

Sprite(wall, (50,200))
Sprite(brownTriangle)
Sprite(pinkDoor,(120,350))
Sprite(blueWindow,(320,300))
App().run()
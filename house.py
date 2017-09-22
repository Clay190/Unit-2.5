#Clay Kynor
#9/20/17
#house.py - house picture

from ggame import *

brown = Color(0x8B540F,1)
blueLight = Color(30-144-255)


brownOutline = LineStyle(2,brown)

brownTriangle = PolygonAsset([(250,0),(0,200),(500,200)],brownOutline,brown)
blueWindow = RectangleAsset

Sprite(brownTriangle)
Sprite(blueWindow)
App().run()
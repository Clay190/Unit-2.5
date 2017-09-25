#Clay Kynor
#9/20/17
#germany.py - German flag

from ggame import *

red = Color(0xFF0000,1)
black = Color(0x000000,1)
orange = Color(0xFF8000,1)

redOutline = LineStyle(1,red)
blackOutline = LineStyle(1,black)
orangeOutline = LineStyle(1,orange)

redRectangle = RectangleAsset(500,150,redOutline,red)
blackRectangle = RectangleAsset(500,150,blackOutline,black)
orangeRectangle = RectangleAsset(500,150,orangeOutline,orange)

Sprite(orangeRectangle,(0,150))
Sprite(blackRectangle)
Sprite(redRectangle,(0,300))
App().run()
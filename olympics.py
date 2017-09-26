#Clay Kynor
#9/26/17
#olympics.py 

from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
yellow = Color(0xFFFF00,1)
white = Color(0xFFFFFF,1)

redOutline = LineStyle(5,red)
greenOutline = LineStyle(5,green)
blueOutline = LineStyle(5,blue)
blackOutline = LineStyle(5,black)
yellowOutline = LineStyle(5,yellow)

redCircle = CircleAsset(100,redOutline,white)
greenCircle = CircleAsset(100,greenOutline,white)
blueCircle = CircleAsset(100,blueOutline,white)
blackCircle = CircleAsset(100,blackOutline,white)
yellowCircle = CircleAsset(100,yellowOutline,white)


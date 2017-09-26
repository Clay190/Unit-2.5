#Clay Kynor
#9/26/17
#warmup5.py

from ggame import *

blue = Color(0x0000FF,1)
yellow = Color(0xFFFF00,1)

yellowOutline = LineStyle(3,yellow)


yellowDiamond = PolygonAsset([(200,0),(300,100),(200,200),(100,100)], yellowOutline,yellow)
text = TextAsset("Clay", fill=blue,style="bold 20pt Times")

Sprite(yellowDiamond)
Sprite(text,(150,75))
App().run()
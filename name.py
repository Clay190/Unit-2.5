#Clay Kynor
#9/26/17
#name.py

from ggame import *

name=input("Please enter your name")
code=input("Enter an RGB color code with a 0x in front of it!")

color = Color(code,1)
black = Color(0x000000,1)

colorOutline = LineStyle(1,color)

text = TextAsset(name, fill=black,style="bold 20pt Times")
backround = RectangleAsset(3000,2000,colorOutline,color)

Sprite(backround)
Sprite(text,(450,250))
App().run()
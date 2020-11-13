from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

img = Image.open("xmasCard.png")
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
# If a font is already installed in your system, you can 
# just give its name
font = ImageFont.truetype("ArialCEMTBLACK.ttf", 14)
# draw.text((x, y),"Sample Text",(r,g,b))
# x, y is the top-left coordinate
draw.text((260, 290),"From",(0,0,0),font=font)
draw.text((260, 390),"To",(0,0,0),font=font)
draw.text((160, 390),"Description",(0,0,0),font=font)
img.save('sample-out.png')

import pandas
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

df = pandas.read_csv('xmasList.csv')
# font = ImageFont.truetype("ArialCEMTBLACK.ttf", 48)
font = ImageFont.truetype("WorkSans-SemiBold.ttf", 48)

# for x in range(len(df)):
#     img = Image.open("xmasCard.png")
#     draw = ImageDraw.Draw(img)

#     #('To')
#     y = df.iloc[x,0]
#     draw.text((260, 390),y,(0,0,0),font=font)

#     #('From')
#     z = df.iloc[x,1]
#     draw.text((260, 290),z,(0,0,0),font=font)

#     #('Description')
#     w = df.iloc[x,2]
#     draw.text((160, 390),w,(0,0,0),font=font)

#     img.save('sample-out(%d).png' % x)

img = Image.open("xmasCard.png")
draw = ImageDraw.Draw(img)

#('To')
y = df.iloc[0,0]
draw.text((100, 150),y,(0,0,0),font=font)

#('From')
z = df.iloc[0,1]
draw.text((100, 80),z,(0,0,0),font=font)

#('Description')
w = df.iloc[0,2]
draw.text((100, 220),w,(0,0,0),font=font)

#('Canada')
draw.text((100, 290),w,(0,0,0),font=font)

#('Ticket #s')
draw.text((110, 1230),w,(0,0,0),font=font)

#('Ticket #s')
draw.text((110, 1285),w,(0,0,0),font=font)

#('Ticket #s')
draw.text((110, 1340),w,(0,0,0),font=font)

#('Ticket #s')
draw.text((110, 1395),w,(0,0,0),font=font)

#('Ticket #s')
draw.text((110, 1450),w,(0,0,0),font=font)

#('Ticket #s')
draw.text((550, 1450),w,(0,0,0),font=font)

img.save('sample-out.png')
    


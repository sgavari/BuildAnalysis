import os
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
 
# Loading Fonts….
# Note the following line works on Ubuntu 12.04
# On other operating systems you should set the correct path
# To the font you want to use.
font = ImageFont.truetype("arial.ttf", 100 , encoding="unic")
 
# Opening the file gg.png
imageFile = r"C:\Users\Sgavari\Desktop\one Button upgrade\WINInstaller\Resources\ktwall8.png"
im1=Image.open(imageFile)
W, H = (1250,100)
msg = "Wafer Inspector Upgrade"
# Drawing the text on the picture
draw = ImageDraw.Draw(im1)
w, h = draw.textsize(msg)
draw.text(((W-w)/2,(H-h)/2),msg,(0,0,0,0),align='center',font=font)
draw = ImageDraw.Draw(im1)

im1.save("C:\\Users\\Sgavari\\Desktop\\one Button upgrade\\WINInstaller\\Resources\\ktwall81.png")

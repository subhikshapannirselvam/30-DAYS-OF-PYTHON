from PIL import Image,ImageDraw,ImageFont
import pandas as pd
import os
to_read=pd.read_csv("name_details.csv")
font=ImageFont.truetype('arial.ttf',30)
for index,j in to_read.iterrows():
    img=Image.open("certificate_template.jpg")
    draw=ImageDraw.Draw(img)
    draw.text(xy=(305,330),text='{}'.format(j['name']),fill=(250,105,180),font=font)
    img.save("certificates/{}.jpg".format(j["name"]))

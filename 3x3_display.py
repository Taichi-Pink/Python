import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

path = []
filename = '00000008.png'
path.append('/home/ziyi/Desktop/drago/'+filename)
path.append('/home/ziyi/Desktop/durand/'+filename)
path.append('/home/ziyi/Desktop/gu/'+filename)
path.append('/home/ziyi/Desktop/drago/'+filename)
path.append('/home/ziyi/Desktop/durand/'+filename)
path.append('/home/ziyi/Desktop/gu/'+filename)
path.append('/home/ziyi/Desktop/drago/'+filename)
path.append('/home/ziyi/Desktop/durand/'+filename)
path.append('/home/ziyi/Desktop/gu/'+filename)

im = Image.open(path[0])
width, high = im.size #get image size
new_im = Image.new('RGB', (3*width+120, 3*high+120+50), (255, 255, 255, 0))
#writing text on image
writer = ImageDraw.Draw(new_im)
fnt = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 20, encoding='unic')# font
writer.text((350,0), filename,font=fnt, fill='black')

index = 0
for i in range(30, 3*width+120, high+30):
    for j in range(80, 3*high+120, width+30):
        im = Image.open(path[index])
        tone = path[index].split('/', 5)[4]  #change
        writer.text((100+i, j-20), tone, font=fnt, fill='black')
        new_im.paste(im, (i,j))
        index += 1

# new_im.save()
new_im.show()
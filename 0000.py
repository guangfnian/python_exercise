#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
im = Image.open(input('Please drag the picture here...\n'))
num = int(input('Please input the number...\n'))
w, h = im.size
font = ImageFont.truetype('arial.ttf',36)
draw = ImageDraw.Draw(im)
if num <= 0:
	print('Error! The number should be larger than 0')
elif num < 10:
	draw.text((w-25, 5), str(num), font = font, fill = (255,0,0))
elif num < 100:
	draw.text((w-50, 5), str(num), font = font, fill = (255,0,0))
else:
	draw.text((w-75, 5), '99+', font = font, fill = (255,0,0))
im.save('hhh.jpg', 'jpeg')

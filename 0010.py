#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

def rand_color():
	return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

def rand_chr():
	return chr(random.randint(65, 90))

w, h, num = 200, 100, 4
im = Image.new('RGB', (w, h), (255, 255, 255))
draw = ImageDraw.Draw(im)
font = ImageFont.truetype('arial.ttf', 50)
for x in range(w):
	for y in range(h):
		draw.point((x, y), fill = rand_color())
for i in range(num):
	draw.text((i*50, 20), rand_chr(), font = font, fill = rand_color())
im = im.filter(ImageFilter.BLUR)
im.save("code.jpg", 'jpeg')

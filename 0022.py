#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from PIL import Image
W, H = 750, 1334 #iPhone 6
#W, H = 1080, 1920 #iPhone 6 plus
os.path.abspath('.')
targetDir = input('Please drag the folder here...\n')
for pic in os.listdir(targetDir):
	try:
		tmp = os.path.join(targetDir, pic)
		im = Image.open(tmp)
		w, h = im.size
		if W >= w and H >= h:
			continue
		x = max(w//W, h//H) + 1
		im.thumbnail((w//x, h//x))
		im.save(os.path.splitext(tmp)[0]+'_resize.jpg', 'jpeg')
	except:
		continue

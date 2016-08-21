#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont

picture_name = 'wangfangpeng.jpg'
saved_name = 'new_wang.jpg'
windows_font = 'Arial.ttf'
color = (255, 0, 0)

def draw_text(text, fill_color, windows_font):
	try:
		im = Image.open(picture_name)
		x, y = im.size
		print "The size of the image is"
		print(im.format, im.size, im.mode)
#		im.show()

		draw = ImageDraw.Draw(im)
		font = ImageFont.truetype(windows_font, 35)
		draw.text((x-20, 7), text, fill_color, font)

		im.save(saved_name)
		im.show()

	except:
		print "Unable to load image"

if __name__ == "__main__":
	number = str(4)
	draw_text(number, color, windows_font)

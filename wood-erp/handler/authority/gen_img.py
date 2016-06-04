#!/usr/bin/env python
#coding=utf-8

import random
import Image, ImageDraw, ImageFont, ImageFilter

_letter_cases = "abcdefghjkmnpqrstuvwxy" # 小写字母，去除可能干扰的i，l，o，z
_upper_cases = _letter_cases.upper() # 大写字母
_numbers = ''.join(map(str, range(3, 10))) # 数字
init_chars = ''.join((_letter_cases, _upper_cases, _numbers))
init_chars_len = len(init_chars)

def gen_img(str_data):
    font_type="/usr/share/fonts/SourceCodePro-Bold.ttf" 
    font_size = 45
    font = ImageFont.truetype(font_type, font_size)
    size = (150, 50)
    width, height = size # 宽，高
    bg_color = (255, 255, 255)
    fg_color = (0, 191, 255)
    img = Image.new("RGB", size, bg_color) # 创建图形
    draw = ImageDraw.Draw(img) # 创建画笔
    create_lines(draw, (5, 10), width, height)
    create_points(draw, 2, width, height)
    draw.text((5, -3), str_data, font=font, fill=fg_color)
    return img.tostring('jpeg', 'RGB')
    
def create_lines(draw, n_line, width, height):
    '''绘制干扰线'''
    line_num = random.randint(n_line[0],n_line[1]) # 干扰线条数
    for i in range(line_num):
        # 起始点
        begin = (random.randint(0, width), random.randint(0, height))
        #结束点
        end = (random.randint(0, width), random.randint(0, height))
        draw.line([begin, end], fill=(0, 0, 0))

def create_points(draw, point_chance, width, height):
    '''绘制干扰点'''
    chance = min(100, max(0, int(point_chance))) # 大小限制在[0, 100]
    for w in xrange(width):
        for h in xrange(height):
            tmp = random.randint(0, 100)
            if tmp > 100 - chance:
                draw.point((w, h), fill=(0, 0, 0))


if __name__ == "__main__":
    gen_img("/tmp/test_gen_img.jpg", ("Tel:18575532201", "Email:baiheng.2011@gmail.com"))

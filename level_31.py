from PIL import Image
import numpy as np
import requests

"""
点击图片
Username: kohsamui
Password: thailand

新的图片是Mandelbrot集合，可查看https://en.wikipedia.org/wiki/Mandelbrot_set
"""

def get_image():
    img_url = 'http://www.pythonchallenge.com/pc/rock/mandelbrot.gif'
    data = requests.get(img_url, auth=('kohsamui', 'thailand')).content
    open('./image/mandelbrot.gif', 'wb').write(data)

def get_done(image):
    left = 0.34
    bottom = 0.57
    width = 0.036
    height = 0.027
    max = 128

    w, h = image.size
    xstep = width / w
    ystep = height / h

    result = []

    for y in range(h - 1, -1, -1):
        for x in range(w):
            c = complex(left + x * xstep, bottom + y * ystep)
            z = 0 + 0j
            for i in range(max):
                z = z * z + c
                if abs(z) > 2:
                    break
            result.append(i)

    image2 = image.copy()
    image2.putdata(result)
    # image2.show()

    diff = [(a - b) for a, b in zip(image.getdata(), image2.getdata()) if a != b]
    print(len(diff))

    plot = Image.new('L', (23, 73))
    plot.putdata([(i < 16) and 255 or 0 for i in diff])
    plot.resize((230, 730)).show()
    plot.resize((230, 730)).save('./image/level_31_res.png')

if __name__ == '__main__':
    # get_image()
    image = Image.open('./image/mandelbrot.gif')
    get_done(image)
    """
    得到的图片是Arecibo_message
    参考https://en.wikipedia.org/wiki/Arecibo_message
    """
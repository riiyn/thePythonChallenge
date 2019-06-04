from PIL import Image
from io import BytesIO
import requests, re

img_url = "http://www.pythonchallenge.com/pc/def/oxygen.png"
img = Image.open(BytesIO(requests.get(img_url).content))
# for i in range(img.width):
#     midPixel = img.getpixel((i, img.height >> 1))
#     print(midPixel)
midPixel = [img.getpixel((i, img.height >> 1)) for i in range(0, img.width, 7)]
code = [r for r, g, b, a in midPixel if r==g==b]
print("".join(map(chr, code)))

nums = re.findall("\d+", "".join(map(chr, code)))
print("".join(map(chr, map(int, nums))))
from PIL import Image
from io import BytesIO
import bz2, requests, keyword

img_url = "http://www.pythonchallenge.com/pc/hex/zigzag.gif"
image = Image.open(BytesIO(requests.get(img_url, auth=('butter', 'fly')).content))
palette = image.getpalette()[::3]
table = bytes.maketrans(bytes([i for i in range(256)]), bytes(palette))
raw = image.tobytes()
trans = raw.translate(table)
zipped = list(zip(raw[1:], trans[:-1]))

diff = list(filter(lambda p: p[0] != p[1], zipped))
indices = [i for i, p in enumerate(zipped) if p[0] != p[1]]

res_img = Image.new('RGB', image.size)
colors = [(255, 255, 255)] * len(raw)
for i in indices:
    colors[i] = (0, 0, 0)
res_img.putdata(colors)
res_img.save("./image/level_27_result.jpg")
# res_img.show()

s = [t[0] for t in diff]
text = bz2.decompress(bytes(s))
words = text.decode().split(' ')
for w in set(words):
    if not keyword.iskeyword(w):
        print(w)

"""
username: repeat
password: switch
"""

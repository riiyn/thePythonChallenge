from io import BytesIO
from PIL import Image

import requests

image_url = "http://www.pythonchallenge.com/pc/return/wire.png"
content = requests.get(image_url, auth = ('huge', 'file')).content
image = Image.open(BytesIO(content))
print(image.size)

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
out = Image.new('RGB', [100, 100])
x, y, p = -1, 0, 0
d = 200
while d / 2 > 0:
    for v in delta:
        steps = d // 2
        for s in range(steps):
            x, y = x + v[0], y + v[1]
            out.putpixel((x, y), image.getpixel((p, 0)))
            p += 1
        d -= 1
out.save("./image/level_14_result.jpg")
# out.show()
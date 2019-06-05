from PIL import Image
from io import BytesIO

import numpy
import requests

image_url = "http://www.pythonchallenge.com/pc/return/mozart.gif"
content = requests.get(image_url, auth = ('huge', 'file')).content
image = Image.open(BytesIO(content))

shifted = [bytes(numpy.roll(row, -row.tolist().index(195)).tolist()) for row in numpy.array(image)]
image = Image.frombytes(image.mode, image.size, b"".join(shifted))
image.save("./image/level_16_result.png")
image.show()

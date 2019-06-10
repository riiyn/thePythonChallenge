import requests
from io import BytesIO
from PIL import Image

img_url = "http://www.pythonchallenge.com/pc/ring/bell.png"
image = Image.open(BytesIO(requests.get(img_url, auth=('repeat', 'switch')).content))
green  = list(image.split()[1].getdata())
diff = [abs(a - b) for a, b in zip(green[0::2], green[1::2])]
filtered = list(filter(lambda x: x != 42, diff))
print(bytes(filtered).decode())
# whodunnit().split()[0] ?
# Guido van Rossum
print("the answer is : " + "Guido van Rossum".split()[0].lower())
# guido

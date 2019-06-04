from io import BytesIO
from PIL import Image

image = Image.open("./image/cave.jpg")
width, height = image.size
even = Image.new('RGB', (width >> 1, height >> 1))
odd = Image.new('RGB', (width >> 1, height >> 1))

for i in range(width):
    for j in range(height):
        imgPixle = image.getpixel((i, j))
        if (i + j) & 1 == 1:
            odd.putpixel((i >> 1, j >> 1), imgPixle)
        else:
            even.putpixel((i >> 1, j >> 1), imgPixle)

even.show()
odd.show()
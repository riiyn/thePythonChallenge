import requests
from io import BytesIO
from PIL import Image, ImageDraw

def get_gif():
    url = "http://www.pythonchallenge.com/pc/hex/white.gif"
    image = Image.open(BytesIO(requests.get(url, auth=('butter', 'fly')).content))
    return image


def solve(image):
    new_img = Image.new('RGB', (500, 200))
    draw = ImageDraw.Draw(new_img)
    cx, cy = 0, 100
    for frame in range(image.n_frames):
        image.seek(frame)
        left, upper, right, lower = image.getbbox()

        dx = left - 100
        dy = upper - 100

        if dx == dy == 0:
            cx += 50
            cy = 100
        cx += dx
        cy += dy
        draw.point([cx, cy])

    new_img.show()
    new_img.save("./image/level_22_result.jpg")

if __name__ == '__main__':
    image = get_gif()
    solve(image) # bonus
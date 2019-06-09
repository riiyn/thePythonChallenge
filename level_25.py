from urllib import request as req
from io import BytesIO
from PIL import Image
import wave, base64

url = 'http://www.pythonchallenge.com/pc/hex/lake%i.wav'
cred = base64.b64encode(b"butter:fly")
image = Image.new('RGB', (300, 300))

for i in range(25):
    request = req.Request(url % (i + 1))
    request.add_header("Authorization", "Basic %s" % cred.decode())
    print("正在下载 %i / %i" % (i + 1, 25))
    response = req.urlopen(request).read()
    waves = wave.open(BytesIO(response))
    patch = Image.frombytes('RGB', (60, 60), waves.readframes(waves.getnframes()))
    pos = (60 * (i % 5), 60 * (i // 5))
    image.paste(patch, pos)

image.save("./image/level_25_result.jpg")
image.show() # decent
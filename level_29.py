from urllib.request import Request, urlopen
import bz2, base64

request = Request("http://www.pythonchallenge.com/pc/ring/guido.html")
request.add_header('Authorization', 'Basic %s' % base64.b64encode(b'repeat:switch').decode())
raw = urlopen(request).read().splitlines()[12:]
data = bytes([len(i) for i in raw])
print(bz2.decompress(data).decode())
# Isn't it clear? I am yankeedoodle!
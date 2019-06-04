import requests
import re
from PIL import Image, ImageDraw

url = "http://www.pythonchallenge.com/pc/return/good.html"
content = requests.get(url=url, auth = ('huge', 'file')).text
# print(content)

pattern = re.compile(r"(\d{2,3})")
nums = re.findall(pattern, content)
nums = list(map(int, nums))
nums.remove(nums[0])
nums.remove(nums[0])
# print(nums)

img = Image.new('RGB', (800, 800))
draw = ImageDraw.Draw(img)
draw.polygon(nums, 'white')
img.show()
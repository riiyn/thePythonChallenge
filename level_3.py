import requests
import re

url = "http://www.pythonchallenge.com/pc/def/equality.html"
content = requests.get(url).text
text = content.split("<!--")
if len(text) > 0:
    text = text[1].split("-->")
if len(text) > 0:
    text = text[0]
pattern = re.compile(r'[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]')
result = re.findall(pattern, text)

res = []
for item in result:
    lower = re.findall(r"[a-z]", item)
    if len(lower) > 2:
        res.append(lower[1])
print("".join(res))
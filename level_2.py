import collections
import requests
import re

def get_s():
    url = "http://www.pythonchallenge.com/pc/def/ocr.html"
    content = requests.get(url).text
    # pattern = re.compile(r'.*<!--(.*)-->.*')
    # text = re.findall(pattern, content)
    text = content.split('-->')
    if len(text) > 2:
        text = text[1].split('<!--')
    if len(text) > 1:
        return text[1]


def count(s):
    lit = []
    lit_num = []
    for item in s:
        if item in lit:
            continue
        lit.append(item)

    for item in lit:
        num = s.count(item)
        lit_num.append(num)
    return collections.OrderedDict(zip(lit, lit_num))

s = get_s()
dic = count(s)
for k, v in  dic.items():
    print(k, '=', v)
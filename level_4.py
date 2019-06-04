from urllib import request
from bs4 import BeautifulSoup

def challenge(nothing):
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}".format(nothing)
    response = request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'lxml')
    body_text = soup.find('body').text
    noth = (body_text.split('.')).pop()

    if 'html' == noth:
        print(body_text)
    else:
        print(body_text)
        noth = (body_text.split(' ')).pop()
        try:
            if isinstance(int(noth), int):
                return challenge(noth)
        except ValueError:
            noth = int(nothing) / 2
            print(noth)
            return challenge(noth)

if __name__ == '__main__':
    challenge('12345')
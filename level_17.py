from urllib.request import urlopen, Request
from urllib.parse import quote_plus, unquote_to_bytes
from xmlrpc.client import ServerProxy
import re, bz2

def get_first_cookie():
    info = ""
    response = urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php")
    cookie = response.getheader("Set-Cookie")
    info += re.search('info=(.*?);', cookie).group(1)
    print(info)
    return info

def get_cookies(url, start_num):
    info = ''
    while(True):
        response = urlopen(url + '?busynothing={0}'.format(start_num))
        response_str = response.read().decode('utf-8')
        cookie = response.getheader("Set-Cookie")
        info += re.search('info=(.*?);', cookie).group(1)
        match = re.search('the next busynothing is (\d+)', response_str)
        print(match)
        if match == None:
            break
        else:
            start_num = match.group(1)
    res = unquote_to_bytes(info.replace("+", " "))
    print(res)
    print(bz2.decompress(res).decode())

def phoneBook(call_name):
    conn = ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
    print(conn.phone(call_name))

def get_final_answer(url, message):
    request = Request(url, headers={"Cookie" : "info=" + quote_plus(message)})
    print(urlopen(request).read().decode())

if __name__ == '__main__':
    # print(get_first_cookie()) # you+should+have+followed+busynothing...

    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
    start_num = "12345"
    # get_cookies(url, start_num)
    """
    is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.
    
    “26th”，”flowers”，这些信息都与Mozart那一关有关联。Mozart的父亲是Leopold Mozart. 
    """

    callName = "Leopold"
    # phoneBook(callName)

    final_url = "http://www.pythonchallenge.com/pc/stuff/violin.php"
    message = "the flowers are on their way"
    get_final_answer(final_url, message)


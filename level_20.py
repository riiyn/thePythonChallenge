import base64, re
from urllib import request as req

def get_range():
    request = req.Request("http://www.pythonchallenge.com/pc/hex/unreal.jpg")
    cred = base64.b64encode(b"butter:fly")
    request.add_header("Authorization", "Basic %s" % cred.decode())
    print(request.headers)

    response = req.urlopen(request)
    print(response.headers)
    print("***********************************************************")
    return request, response

def get_range_space(request, response):
    pattern = re.compile("bytes (\d+)-(\d+)/(\d+)")
    content_range = response.headers['content-range']
    (start, end, length) = pattern.search(content_range).groups()

    while True:
        try:
            request.headers['Range'] = 'bytes=%i-' % (int(end) + 1)
            response = req.urlopen(request)
            print(response.headers)
            print(response.read().decode())
            (start, end, length) = pattern.search(response.headers['content-range']).groups()
        except:
            break

    return length

def get_after_length(request, response, length):
    request.headers['Range'] = 'bytes=%i-' % (int(length) + 1)
    response = req.urlopen(request)
    content = response.read().decode()
    print("*************************************************************")
    print(response.headers)
    print(content)
    print(content[::-1])
    print("The 'nickname' is 'invader', so password is " + ''.join(reversed('invader')))

def reverse_search(request, response):
    request.headers['Range'] = 'bytes=2123456743-'
    response = req.urlopen(request)
    print(response.headers)
    print(response.read().decode())

def solve(request, response, param):
    request.headers['Range'] = 'bytes=' + param + '-'
    response = req.urlopen(request)

    with open("./file/level_21.zip", "wb") as file:
        file.write(response.read())

    print("Done...")

if __name__ == '__main__':
    request, response = get_range()
    # length = get_range_space(request, response)
    # get_after_length(request, response, length)
    # reverse_search(request, response)
    param = "1152983631"
    solve(request, response, param)
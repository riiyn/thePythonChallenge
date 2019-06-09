import requests, re, hashlib

def get_email():
    url = "http://www.pythonchallenge.com/pc/hex/bin.html"
    content = requests.get(url, auth=('butter', 'fly')).text
    email = re.search(r'\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}', content)
    if email != None:
        email = email.group(0)
    return email

def search_save(data, md5_code):
    for i in range(len(data)):
        for j in range(256):
            new_data = data[:i] + bytes([j]) + data[i + 1:]
            if hashlib.md5(new_data).hexdigest() == md5_code:
                open("./file/repaired.zip", "wb").write(new_data)
                print("*****************Done*****************")
                return

if __name__ == '__main__':
    # print(get_email())
    """
    发送邮件，得到回复
    Never mind that.

    Have you found my broken zip?

    md5: bbb8b499a0eef99b52c7f13f4e78c24b

    Can you believe what one mistake can lead to?
    """

    md5_code = "bbb8b499a0eef99b52c7f13f4e78c24b"
    data = open("./file/maze/mybroken.zip", "rb").read()
    search_save(data,  md5_code) # 得到speed
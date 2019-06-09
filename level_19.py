import base64, wave
import requests

def get_string():
    url = "http://www.pythonchallenge.com/pc/hex/bin.html"
    content = requests.get(url, auth=('butter', 'fly')).text
    array = content.split("Content-transfer-encoding: base64")
    if len(array) > 1:
        string = array[1]
    string = string.split("--===============1295515792==--")
    if len(string) > 0:
        string = string[0].strip()
    file = open("./file/email.txt", "wt")
    file.write(string)
    file.close()

def get_res():
    message = open("./file/email.txt", "rb").read()
    open('./file/indian.wav', 'wb').write(base64.decodebytes(message))

    india = wave.open('./file/indian.wav', 'r')
    india_frames = india.readframes(india.getnframes())
    india_swap = wave.open("./file/indian_swap.wav", "w")
    india_swap.setnchannels(1)
    india_swap.setframerate(india.getframerate())
    india_swap.setsampwidth(india.getsampwidth())

    india_swap_frames = []
    for i in range(0, len(india_frames), 2):
        # 每一帧前后颠倒
        india_swap_frames.append(india_frames[i + 1])
        india_swap_frames.append(india_frames[i])
    india_swap_frames = ''.join('%s' %id for id in india_swap_frames).encode()
    india_swap.writeframes(india_swap_frames)
    india_swap.close()
    india.close()

if __name__ == '__main__':
    # get_string()
    get_res()
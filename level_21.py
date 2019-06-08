import zlib, bz2

def uncompress():
    with open("./file/level_21/package.pack", "rb") as file:
        data = file.read()

        while True:
            if data.startswith(b'x\x9c'):
                data = zlib.decompress(data)
            elif data.startswith(b'BZh'):
                data = bz2.decompress(data)
            elif data.endswith(b'\x9cx'):
                data = data[::-1]
            else:
                break
        print(data.decode()[::-1])

def solve():
    """
    add logging
    :return:
    """
    result = ""
    with open("./file/level_21/package.pack", "rb") as file:
        data = file.read()

        while True:
            if data.startswith(b'x\x9c'):
                data = zlib.decompress(data)
                result += ' '
            elif data.startswith(b'BZh'):
                data = bz2.decompress(data)
                result += '#'
            elif data.endswith(b'\x9cx'):
                data = data[::-1]
                result += '\n'
            else:
                break
        print(result)

if __name__ == '__main__':
    uncompress()
    #  look at your logs

    solve()
    # copper


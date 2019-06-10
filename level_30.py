from PIL import Image

with open('./file/yankeedoodle.csv') as file:
    data = [x.strip() for x in file.read().split(',')]
    length = len(data)
    print(length)

    factors = [x for x in range(2, length) if length % x == 0]
    print(factors)
    # [53, 139]

    img = Image.new('F', (53, 139))
    img.putdata([float(x) for x in data], 256)
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    img = img.transpose(Image.ROTATE_90)
    img.save('./image/level_30_res.gif')
    # img.show()

    a = data[0::3]
    b = data[1::3]
    c = data[2::3]

    res = bytes([int(x[0][5] + x[1][5] + x[2][6]) for x in zip(a, b, c)])
    print(res.decode())

    # grandpa
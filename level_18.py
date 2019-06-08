import gzip, difflib

def getRes():
    data = gzip.open("./file/deltas.gz")
    d1, d2 = [], []
    for line in data:
        d1.append(line[:53].decode() + "\n")
        d2.append(line[56:].decode())
    compare = difflib.Differ().compare(d1, d2)
    f = open("./image/f.png", "wb")
    f1 = open("./image/f1.png", "wb")
    f2 = open("./image/f2.png", "wb")

    for line in compare:
        bs = bytes([int(o, 16) for o in line[2:].strip().split(" ") if o])
        if line[0] == "+":
            f1.write(bs)
        elif line[0] == "-":
            f2.write(bs)
        else:
            f.write(bs)

    f.close()
    f1.close()
    f2.close()

if __name__ == '__main__':
    print(gzip.open("./file/deltas.gz").read().decode())  # 打印发现数据分左右两栏
    getRes()
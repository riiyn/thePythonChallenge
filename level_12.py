data = open("./file/evil2.gfx", "rb").read()
print(data)
for i in range(5):
    open('./image/%d.jpg' % i ,'wb').write(data[i::5])
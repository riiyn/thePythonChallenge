import zipfile

file_zip = zipfile.ZipFile("./file/channel.zip")
files = file_zip.namelist()
lst = []

def item(start):
    if start in files:
        with file_zip.open(start) as f:
            content = f.read().decode()
            comment = file_zip.getinfo(start).comment
            lst.append(comment.decode())
            print(content)
            result = '{}.txt'.format(content.split(' ').pop())
        return item(result)
    else:
        result = start.split('.')
        print('the result is：', result[0])

if __name__ == '__main__':
    item('90052.txt')
    result = ''.join(lst)
    print(result)
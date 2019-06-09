import requests
from io import BytesIO
from PIL import Image

def get_points(maze):
    width, height = maze.size
    for i in range(width): print(maze.getpixel((i, 0)))  # 打印顶部像素
    print("***************************************")
    for i in range(width): print(maze.getpixel((i, height - 1)))  # 打印底部像素
    print("***************************************")
    for i in range(width): print(maze.getpixel((i, i)))  # 打印内部像素

def get_shortest_path(maze):
    """
    用BFS解迷宫
    :param maze:
    :return:
    """
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    white = (255, 255, 255, 255)
    width, height = maze.size
    next_map = {}
    entrance_point = (width - 2, 0)
    exit_point = (1, height - 1)
    queue = [exit_point]
    while queue:
        pos = queue.pop(0)
        if pos == entrance_point:
            break
        for d in directions:
            temp = (pos[0] + d[0], pos[1] + d[1])
            if not temp in next_map and 0 <= temp[0] < width and 0 <= temp[1] < height and maze.getpixel(temp) != white:
                next_map[temp] = pos
                queue.append(temp)
    path = []
    while pos != exit_point:
        path.append(maze.getpixel(pos)[0])
        pos = next_map[pos]

    print(path[1::2])
    open("./file/maze.zip", "wb").write(bytes(path[1::2]))

if __name__ == '__main__':
    url = "http://www.pythonchallenge.com/pc/hex/maze.png"
    maze = Image.open(BytesIO(requests.get(url, auth=('butter', 'fly')).content))

    # get_points(maze)
    get_shortest_path(maze) # 解压maze.zip得到lake

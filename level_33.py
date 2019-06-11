from PIL import Image
from scipy.stats import itemfreq
from pprint import pprint
import math, requests
import numpy as np

def get_img():
    url = "http://www.pythonchallenge.com/pc/rock/beer2.png"
    data = requests.get(url, auth=('kohsamui', 'thailand')).content
    open('./image/beer2.png', 'wb').write(data)

def get_done(im):
    im_data = np.array(list(im.getdata()))
    im_data_stat = itemfreq(im_data)
    pprint(im_data_stat)
    print("*********************************************************")
    pprint([np.sqrt(i) for i in np.cumsum(im_data_stat[:, 1])])

    for i in range(im_data_stat.shape[0] - 2, 0, -2):
        newIm_data = im_data[np.where(im_data < im_data_stat[i, 0])]
        idx_0 = np.where(newIm_data == newIm_data.max())
        idx_1 = np.where(newIm_data != newIm_data.max())
        newIm_data[idx_0] = 0
        newIm_data[idx_1] = 1
        size = int(np.sqrt(len(newIm_data)))
        newIm = Image.new('1', (size, size))
        newIm.putdata(newIm_data)
        newIm.save('./image/level_33/level_33_res%s.png' % i)

if __name__ == '__main__':
    # get_img()
    im = Image.open('./image/beer2.png')
    get_done(im)
    # gremlins
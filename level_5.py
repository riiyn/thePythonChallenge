import pickle
from urllib import request

handle = request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.load(handle)
handle.close()

for elt in data:
    print("".join([e[1] * e[0] for e in elt]))

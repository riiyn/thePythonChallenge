from xmlrpc import client

url = "http://www.pythonchallenge.com/pc/phonebook.php"
proxy = client.ServerProxy(url)
methods = proxy.system.listMethods()
print(methods)
"""
['phone', 'system.listMethods', 'system.methodHelp', 'system.methodSignature', 'system.multicall', 'system.getCapabilities']
"""
print(proxy.system.methodHelp('phone'))
"""
Returns the phone of a person
访问http://www.pythonchallenge.com/pc/return/evil4.jpg得到person=evil=Bert
"""
print(proxy.phone("Bert"))
"""
555-ITALY
555表示US号码
所以key是ITALY
"""
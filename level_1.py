"""
K -> M
O -> Q
E -> G

每个字母后移两位
"""

# s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
s = "map"
def change_str(s):
    if s is 'y':
        return 'a'
    if s is 'z':
        return 'b'
    if s.isalpha() and s not in 'yz':
        return chr(ord(s) + 2)
    return s

new_s = map(change_str, s)
print(''.join(new_s))
a, sub = '1', ''
for i in range(30):
    j = k = 0
    while j < len(a):
        while k < len(a) and a[k] == a[j]:
            k += 1
        sub += str(k - j) + a[j]
        j = k
    a, sub = sub, ''

print(len(a))
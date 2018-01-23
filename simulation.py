import random

def getitem():
    x = random.randint(0,100)
    if x < 10:
        return '*'
    else:
        return '.'

s = ''
last = -1
tj = [0 for i in range(30)]
for i in range(200000):
    x = getitem()
    s += x
    if x == '*':
        if last != -1:
            tj[int((i - last - 1)/5)] += 1
        last = i

print(s)
for i in range(30):
    print(i,'-',(i+4),':',tj[i])
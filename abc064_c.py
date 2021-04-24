N = int(input())
a = list(map(int, input().split()))

cols = {}

def rtnCol(rate):
    if 0 < rate < 400:
        return 'gra'
    elif rate < 800:
        return 'cha'
    elif rate < 1200:
        return 'gre'
    elif rate < 1600:
        return 'sky'
    elif rate < 2000:
        return 'blue'
    elif rate < 2400:
        return 'yel'
    elif rate < 2800:
        return 'ora'
    elif rate < 3200:
        return 'red'
    else:
        return 'rainbow'


for i in range(N):
    color = rtnCol(a[i])
    if color not in cols.keys():
        cols[color] = 0

    cols[color] += 1

#print(cols)

if 'rainbow' not in cols.keys():
    print(len(cols), len(cols))
elif len(cols) == 1:
    print(1,cols['rainbow'])
else:
    print(len(cols)-1,len(cols)+cols['rainbow']-1)

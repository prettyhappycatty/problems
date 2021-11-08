import math
from functools import reduce
def my_gcd(*numbers):
    return reduce(math.gcd, numbers)

import math
N = int(input())

points = []

for i in range(N):
    x,y = map(int, input().split())
    points.append([x,y])

dic = {}
for i in range(N-1):
    for j in range(i+1,N):
        dx = points[i][0]-points[j][0]
        dy = points[i][1]-points[j][1]
        g = my_gcd(dx,dy)
        tup = tuple((dx//g,dy//g))
        if tup not in dic.keys():
            dic[tup] = 0
        dic[tup] += 1
        tup2 = tuple((-dx//g,-dy//g))
        if tup2 not in dic.keys():
            dic[tup2] = 0
        dic[tup2] += 1
#print(dic)
print(len(dic))
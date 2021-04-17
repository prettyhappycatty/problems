import math

N, D = list(map(int, input().split()))
ary_x = []
ary_y = []
for i in range(N):
    tmp = list(map(int, input().split()))
    ary_x.append(tmp)

def dist(x, y, d):
    dist = 0
    for i in range(d):
        dist += (x[i]-y[i])**2
    return math.sqrt(dist)

cnt = 0
for i in range(N):
    for j in range(N):
        #print(i,j)
        if i < j :
            k = dist(ary_x[i], ary_x[j], D)
            #print(i,j, k)
            if k.is_integer():
                #print(True)
                cnt += 1

print(cnt)


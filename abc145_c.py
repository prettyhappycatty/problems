import math, itertools

N = int(input())
x_ = []
y_ = []

for i in range(N):
    x_tmp, y_tmp = list(map(int, input().split()))
    x_.append(x_tmp)
    y_.append(y_tmp)

x_p = list(itertools.permutations(x_, len(x_)))
y_p = list(itertools.permutations(y_, len(y_)))

#print(x_p, y_p)
def calcSum(x_, y_):
    x_bef, y_bef = x_[0], y_[0]
    sum_dist = 0
    for i in range(1, N):
        x_tmp, y_tmp = x_[i], y_[i]
        sum_dist += math.sqrt((x_bef - x_tmp)**2 + (y_bef - y_tmp)**2)
        x_bef, y_bef = x_tmp, y_tmp
    return sum_dist

sum_dist_gl = 0
for x, y in zip(x_p, y_p):
    sum_dist_gl += calcSum(x, y)

print(sum_dist_gl/len(list(x_p)))
#print(sum_dist_gl,len(list(x_p)))
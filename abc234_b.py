import math

N = int(input())
x = []
y = []

for i in range(N):
    X, Y = map(int, input().split())
    x.append(X)
    y.append(Y)

def norm2(x1, y1, x2, y2):
    return (x1-x2)**2+(y1-y2)**2


max2 = 0
for i in range(N):
    for j in range(N):
        max2 = max(norm2(x[i],y[i],x[j],y[j]),max2)

print(math.sqrt(max2))
        


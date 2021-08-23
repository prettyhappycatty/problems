N = int(input())
X = []
Y = []
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)


def katamuki(x,y,x2,y2):
    return float(y-y2)/float(x-x2)

cnt = 0
for i in range(N-1):
    for j in range(i+1, N):
        ka = katamuki(X[i],Y[i],X[j],Y[j])
        if -1<= ka and ka <= 1:
            cnt+=1

print(cnt)
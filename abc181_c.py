

N = int(input())
X = []
Y = []
for i in range(N):
    tmpx, tmpy = map(int, input().split())
    X.append(tmpx)
    Y.append(tmpy)

#同一直線上＝傾き同じ、切片同じ
def get_line_def(x1,y1,x2,y2):
    # y = ax+b a, b 有効数字4桁にする
    if x2 - x1 == 0:#
        a = "a=None"
        b = x1
    else:
        a = (y1 - y2)/(x1 - x2) 
        b = y1 - a * x1
    #a = float(str(a)[0:4])
    #b = float(str(b)[0:4])
    return a, b

ans = {}
for i in range(N-1):
    for j in range(i+1,N):
        a, b = get_line_def(X[i],Y[i],X[j],Y[j])
        #print(i,j,"(", X[i],Y[i],"),(",X[j],Y[j],")",a,b)
        if (a,b) in ans.keys():
            print("Yes")
            exit()
        else:
            ans[tuple((a,b))] = True

print("No")


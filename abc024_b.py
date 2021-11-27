N, T = map(int, input().split())
A = []
for i in range(N):
    tmpA = int(input())
    A.append(tmpA)

cnt = 0
bef_during = 0 #前回のいつまで空いているかを管理
during = 0
bef = A[0]
for i in range(0,N):
    #print(during, bef,bef_during,A[i])
    if during > A[i]:
        cnt += A[i]-bef #A[i]-befの時間は空いていた
        #print("1+", A[i]-bef)
    else:
        cnt+= T
        #print("3+", T)
    bef = A[i]
    bef_during = during
    during =  A[i] + T

print(cnt)
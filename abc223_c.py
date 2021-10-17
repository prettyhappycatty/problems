N = int(input())

T = []
B = []
sum_T = [0]
sum_A = [0]
tmp_sum_T = 0
tmp_sum_A = 0
for i in range(N):
    a, b = map(int, input().split())
    t = a / b
    #print(t)
    tmp_sum_T += t
    tmp_sum_A += a
    T.append(t)
    sum_T.append(tmp_sum_T)
    sum_A.append(tmp_sum_A)
    B.append(b)

#print(T, sum_T[N]) #それぞれの導火線が何秒で燃えるかを管理
#colisionT = sum_T[N] / 2 #ぶつかるときの燃える秒数

for i in range(N+1):
    if sum_T[i]*2 >= sum_T[N]:
        break

#print(i)
#print(sum_T)
#print(sum_A)
#print(B)#もえる速さ

#長さ
#print(sum_A[i-1], sum_T[N], sum_T[N]/2, (sum_T[N]/2-sum_T[i-1]),B[i-1],sum_A[i-1], B[i-1])
ans = sum_A[i-1] + (sum_T[N]/2-sum_T[i-1])*B[i-1]
print(ans)

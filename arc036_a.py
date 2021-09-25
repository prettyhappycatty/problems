N, K = map(int, input().split())
t_ary = []
sum3 = 0
for i in range(N):
    t = int(input())
    t_ary.append(t)
    sum3 += t
    if i >= 2:
        #print(sum3)
        #print(t_ary, t, "sum=", sum3)
        if sum3 < K:
            print(i+1)
            exit()
        sum3 -= t_ary[i-2]

print(-1)
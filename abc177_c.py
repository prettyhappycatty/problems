N = int(input())
A = list(map(int, input().split()))
MOD = 10**9+7

s = [0]
ssum = 0
for i in range(N):
    ssum += A[i]
    s.append(ssum)

#print(s)

cnt = 0
for i in range(N):
    #print(A[i], "*",s[N]-s[i+1])
    tmp = A[i]*(s[N]-s[i+1]) % MOD
    cnt += tmp

print(cnt % MOD)


#cnt2 = 0
#for i in range(N):
#    tmp = 0
#    for j in range(i+1, N):
#        tmp += A[j]
#    print(A[i], "*", tmp)
#    cnt2 += A[i]*tmp

#print(cnt2 % MOD)
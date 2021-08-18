N, T = map(int, input().split())

dic = []

for i in range(N):
    tmpA, tmpT =  map(int, input().split())
    dic.append((tmpA, tmpT))


dic_s = sorted(dic, key=lambda x:x[0], reverse=False)

s = 0
i = 0

if dic_s[i][0] > T:
    print(-1)
    exit()

A_wa = []
A_wa.append(0)
for i in range(N):
    A_wa.append(A_wa[i]+dic_s[i][0]) 

#print(A_wa)

A_wa_rev = []
A_wa_rev.append(0)
for i in range(N-1, -1, -1):
    A_wa_rev.append(A_wa_rev[N-i-1]+dic_s[i][1])

A_wa_rev.reverse()
#print(dic_s)
#print(A_wa)
#print(A_wa_rev)
#print(T)
for i in range(N+1):
#    print(A_wa[i] + A_wa_rev[i])
    if A_wa[i]  >= T:
        print(N-i+1)
        exit()

print(0)
N = int(input())
W = list(map(int, input().split()))

#W.sort()

#print(W)

S = []
sum_S = 0
for i in range(N):
    sum_S += W[i]
    S.append(sum_S)

ans = 10**4
for i in range(0,N-1):
    #print(S[N-1]-S[i],S[i])
    ans = min(ans, abs((S[N-1]-S[i])-(S[i])))

print(ans)
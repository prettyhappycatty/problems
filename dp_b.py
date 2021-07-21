N,K= map(int, input().split())

h = list(map(int, input().split()))

# c2 = h2-h1
# c3 = min(c2, (h3-h1))
# c4 = min(c2+h4-h2, c3+h4-h3) 

ans = [0 for _ in range(N)]

#
for i in range(1,N):
    #print("i=",i)
    if i == 1:
        ans[i] = ans[i-1] + abs(h[i] - h[i-1])
    else:
        m = ans[i-1] + abs(h[i] - h[i-1])
        for j in range(2,K+1):
            #print(ans[i-j] + abs(h[i]-h[i-j]))
            if i-j > -1:
                m = min(ans[i-j] + abs(h[i]-h[i-j]), m)
        #print("min",m)
        ans[i] = m
        #print(ans)

print(ans[N-1])
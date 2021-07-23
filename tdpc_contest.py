N = int(input())
P = list(map(int, input().split()))

#i問目までの得点の通り数をPsum[i]とする

Psum = []

Psum.append([0, P[0]])

for i in range(1, N):
    sumdic = {}
    for ps in Psum[i-1]:
        sumdic[ps] = True
        sumdic[ps+P[i]] = True
    ary = []
    for k,v in sumdic.items():
        ary.append(k)
    Psum.append(ary)

print(len(Psum[N-1]))

    

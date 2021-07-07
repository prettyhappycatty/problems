N = int(input())
S = input()

groups = []
bef = S[0]
tmps = [S[0]]
for i in range(1, len(S)):
    if bef == S[i]:
        tmps.append(S[i])
    else:
        groups.append(tmps)
        tmps = [S[i]]
        bef = S[i]

groups.append(tmps)
#print(groups)
count = 0
for grp in groups:
    l = len(grp)
    #print(l)
    count += l*(l+1)//2

print(N*(N+1)//2 - count)


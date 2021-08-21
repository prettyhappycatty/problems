import itertools

S, K = input().split()
K = int(K)
S = sorted(S,reverse=False)
#print(S)

all = list(itertools.permutations(S, len(S)))

ar = []
for i in range(len(all)):
    lst = list(all[i])
    ar.append(''.join(lst))


ar_sorted = sorted(set(ar))
#print(len(ar_sorted), K)
print(ar_sorted[K-1])


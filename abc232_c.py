import math, itertools

N, M = map(int, input().split())

set1 = set()
for i in range(M):
    a, b = map(int, input().split())
    if a < b:
        set1.add(tuple((a-1,b-1)))
    else:
        set1.add(tuple((b-1,a-1)))

C, D = [], []
for i in range(M):
    c, d = map(int, input().split())
    C.append(c-1)
    D.append(d-1)

p = list(itertools.permutations([i for i in range(N)], N))
#print(C, D)
#print(set1)
for pp in p:
    cnt = 0
    for j in range(M):
        a, b = pp[C[j]], pp[D[j]]
        if a > b:
            tmp = a
            a = b
            b = tmp
        if tuple((a , b)) in set1:
            cnt += 1

    if cnt == M:
        #print(cnt, pp)
        print("Yes")
        exit()

#print(cnt)
print("No")

import itertools

N = int(input())
A = list(map(int, input().split()))

lst = list(itertools.combinations(range(N), 2))

#print(lst)

cnt = 0
for l in lst:
    #print(l[0],l[1])
    cnt += A[l[0]]*A[l[1]]

print(cnt)
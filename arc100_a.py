N = int(input())
A = list(map(int, input().split()))

def median(ary):
    ary.sort()
    if len(ary) % 2 == 1:
        return ary[len(ary)//2]
    else:
        return (ary[len(ary)//2-1] + ary[len(ary)//2])//2

for i in range(N):
    A[i] -= (i+1)

med = median(A)
#print(med)

cnt = 0
for i in range(N):
    cnt += abs(A[i]-med)

print(cnt)

import sys

sys.setrecursionlimit(10 ** 8)

N = int(input())

A = []
for i in range(2*N+1):
    A.append([0]*(2*N+1))


for i in range(2*N-1):
    tmpA = list(map(int, input().split()))
    A[i][i+1:] = tmpA

print(A)


cand = []


def dfs(done, ans):
    if len(done) == 2*N:
        cand.append(ans)
        return

    for u in range(2*N):
        if u not in done:
            break

    done.add(u)

    for v in range(2*N):
        if v not in done:
            done.add(v)
            ans ^= A[u][v]
            dfs(done, ans)
            done.remove(v)
            ans ^= A[u][v]

    done.remove(u)


dfs(set(), 0)
print(max(cand))

#箱の中の箱

N, X = map(int, input().split())
A = list(map(int, input().split()))

G = [[] for i in range(N-1)]
for i in range(N-1):
	G[i].append(A[i])

#print(G)

def search(i):
	if i == 0:
		return 0
	else:
		for g in G[i-1]:
			return search(g)+1

print(search(X))
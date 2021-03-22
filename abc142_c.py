N = int(input())
X = {int(x)-1:i for i, x in enumerate(input().split())}



for i in range(N):
	print(X.get(i)+1, end=' ')

N = int(input())
S = input()
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

#荷物ループ
cnt = 1
for i in range(N):
	n = 0
	#入る最小の箱ループ
	while 1:
		if A[i] <= B[n]:
			#A[n]をB[i]に入れる
			cnt += 1
			n += 1
			break #次ループへ
		else:
			n += 1
			#箱の番号だけ増やす

print(cnt)



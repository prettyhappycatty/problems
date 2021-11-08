N = int(input())

#なるべく多い500円高価と、5円

cnt = 0
cnt500 = N // 500
cnt += cnt500*1000
rest = N - cnt500*500
cnt5 = rest // 5
cnt += cnt5*5

#print(cnt500, cnt5)

print(cnt)
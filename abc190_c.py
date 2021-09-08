import itertools

N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for i in range(M)]

K = int(input())
CD = [tuple(map(int, input().split())) for i in range(K)]

ans = 0
cnt_product = 0
for balls in itertools.product(*CD):
    #itertools.product デカルト積
    #cnt_product += 1
    balls = set(balls)
    #print(balls)
    cnt = sum(A in balls and B in balls for A, B in AB)
    #print(cnt)
    if ans < cnt:
        ans = cnt

#print(cnt_product)
print(ans)


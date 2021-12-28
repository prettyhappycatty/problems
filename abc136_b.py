N = int(input())

def get_keta(n):
    if n < 10:
        return 1
    elif n < 100:
        return 2
    elif n < 1000:
        return 3
    elif n < 10000:
        return 4
    elif n < 100000:
        return 5
    else:
        return 6

cnt = 0
for i in range(1, N+1):
    if get_keta(i) % 2 == 1:
        cnt += 1

print(cnt)


N, T = list(map(int, input().split()))
t = list(map(int, input().split()))

until = 0
rest_during = 0
for i in range(N):
    now = t[i]
    if until < now:
        rest_during += now-until
    until = now+T


print(until-rest_during)


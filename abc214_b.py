S, T = map(int, input().split())

# a, b, c は1から100
cnt = 0
for a in range(0, 101):
    for b in range(0, 101):
        for c in range(0, 101):
            if a+b+c <= S and a*b*c <= T:
                cnt += 1

print(cnt)
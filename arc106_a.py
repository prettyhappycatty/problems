N = int(input())

# 3 ^ 38 >10^ 18 、5 ^ 26 >10 ^18
# のため、Aは38まで、Bは26まで探索すればいい

for i in range(1, 38):
    for j in range(1, 26):
        if 3 ** i + 5 ** j == N:
            print(i, j)
            exit()

print(-1)
    
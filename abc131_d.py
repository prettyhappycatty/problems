N = int(input())
ab = []
for i in range(N):
    ab.append(tuple((map(int, input().split()))))

#print(ab)

ab_sorted = sorted(ab, key=lambda x:x[1])

#print(ab_sorted)

tt = 0
for t in ab_sorted:
    a = t[0]
    b = t[1]
    tt += a
    if tt > b:
        print("No")
        exit()
print("Yes")
A, B, C = map(int, input().split())

ar = [A,B,C]

arsum = 0
smallest = 101
for i in range(len(ar)):
    arsum += ar[i]
    if ar[i] < smallest:
        smallest = ar[i]

print(arsum-smallest)

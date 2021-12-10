a = []

for i in range(5):
    a.append(int(input()))

k = int(input())

#print(a)

for i in range(5):
    for j in range(i, 5):
        if a[j] - a[i]>k:
            print(":(")
            exit()

print("Yay!")
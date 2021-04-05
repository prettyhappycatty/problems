N = int(input())
T, A = list(map(int, input().split()))
H = list(map(int, input().split()))

nearlest = -1
min_diff_temp = 1000000000
for i in range(N):
    diff_temp = abs(A - (T - 0.006*H[i]))
    if diff_temp < min_diff_temp:
        min_diff_temp = diff_temp
        nearlest = i

print(nearlest+1)
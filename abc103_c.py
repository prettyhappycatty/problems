N = int(input())
a = list(map(int, input().split()))

int_sum = 0
for i in range(N):
    int_sum += a[i]-1

print(int_sum)
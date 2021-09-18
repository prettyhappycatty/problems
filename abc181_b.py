N = int(input())

def sum_ary(a, b):
    return (a + b)*(b-a+1)//2
cnt = 0
for i in range(N):
    tmpA, tmpB = map(int, input().split())
    cnt += sum_ary(tmpA, tmpB)

print(cnt)


t = int(input())


def solve(b5,b6,b7):
    a1 = b7 - b6
    a2 = b7 - b5 
    a3 = b7 - (a1+a2)
    return a1, a2, a3

for i in range(t):
    b = list(map(int, input().split()))
    a1, a2, a3 = solve(b[4],b[5],b[6])
    print(a1,a2,a3)


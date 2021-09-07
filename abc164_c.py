N = int(input())

prize = {}
for i in range(N):
    S = input()
    prize[S] = True

print(len(prize))

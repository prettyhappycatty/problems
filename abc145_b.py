n = int(input())
S = input()

if n % 2 == 1:
    print("No")
    exit()

for i in range(n//2):
    if S[i] != S[n//2+i]:
        print("No")
        exit()

print("Yes")

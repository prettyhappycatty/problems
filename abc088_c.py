a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
a3 = list(map(int, input().split()))

if a1[0]-a2[0] == a1[1] - a2[1] == a1[2] - a2[2] and a3[0]-a2[0] == a3[1] - a2[1] == a3[2] - a2[2] and a3[0]-a1[0] == a3[1] - a1[1] == a3[2] - a1[2]:
    print("Yes")
else:
    print("No")
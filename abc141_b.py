S = input()

for i in range(len(S)):
    if i % 2 == 1:
        if S[i] == "R":
            print("No")
            exit()
    else:
        if S[i] == "L":
            print("No")
            exit()

print("Yes")

S = input()
T = input()

for i in range(len(T)):
    if S[i] == "@":
        if T[i] in "atcoder@":
            continue
        else:
            print("You will lose")
            exit()
    elif T[i] == "@":
        if S[i] in "atcoder@":
            continue
        else:
            print("You will lose")
            exit()
    else:
        if S[i] != T[i]:
            print("You will lose")
            exit()


print("You can win")


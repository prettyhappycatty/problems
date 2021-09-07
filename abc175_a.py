S = input()

r = S.count("R")

if r < 2 or r == 3:
    print(r)
else:
    if S[1] == "R":
        print(2)
    else:
        print(1)
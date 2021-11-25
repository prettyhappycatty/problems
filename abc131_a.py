S = input()

bef = ''
for i in range(len(S)):
    if bef == S[i]:
        print("Bad")
        exit()
    bef = S[i]
print("Good")
S = input()

bef = ""
comma_flg = False
ans = ""
for i in range(len(S)):
    if S[i] == " ":
        comma_flg = True
    else:
        if comma_flg == True:
            ans += ","
            comma_flg = False
        ans += S[i]
    bef = S[i]

print(ans)

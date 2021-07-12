S = input()

users = {}
flg = 0
tmp_user = ""
for i in range(len(S)):
    if flg == 0 and S[i] == "@":#ユーザ名モードin
        flg = 1
        tmp_user = ""
        continue
    elif flg == 1 and S[i].isalpha():#ユーザ名モード継続
        tmp_user += S[i]
    elif flg == 1 and S[i] ==  "@": #ユーザ名モードが継続
        flg = 1
        if len(tmp_user)>0:
            users[tmp_user] = 1
            tmp_user = ""
    elif flg == 1: #ユーザ名モードが途切れた時
        flg = 0
        if len(tmp_user)>0:
            users[tmp_user] = 1
            tmp_user = ""

    if i == len(S)-1 and len(tmp_user)>0:
        users[tmp_user] = 1
        tmp_user = ""

if len(users) == 0:
    exit()


#print(users)
if len(list(users)) == 0:
    exit()

users_sorted = sorted(users.items(), key=lambda x:x[0])
#print(users_sorted)
for a,b in enumerate(users_sorted):
    print(b[0])


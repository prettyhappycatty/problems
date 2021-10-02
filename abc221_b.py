S = input()
T = input()

cnt = 0
diff_id = []
for i in range(len(S)):
    if S[i] != T[i]:
        cnt += 1
        diff_id.append(i)

if cnt == 0:
    print("Yes")
elif cnt >= 3 or cnt == 1:
#cntが3以上、1はNo
    print("No")
else:
#cntが2の場合、隣り合っていて入れ替えればOKかを確認する
    if diff_id[0]+1 == diff_id[1]:
        if S[diff_id[0]] == T[diff_id[1]] and S[diff_id[1]] == T[diff_id[0]]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

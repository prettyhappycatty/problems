H, W,A, B = map(int, input().split())

T = []
for i in range(H):
    tmp = []
    for j in range(W):
        if (j < A and (i - B)>=0) or (j >= A and (i - B) < 0):
            tmp.append("1")
        else:
            tmp.append("0")

    print(''.join(tmp))
    #T.append(tmp)

#print(T)
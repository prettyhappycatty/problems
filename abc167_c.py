# bit全探索

def bit_list(n):#n桁の2進数をリストアップ
    ret = []
    for i in range(2**n):
        s = ""
        j = i
        while j != 0:
            rest = j % 2
            s = str(rest) + s
            j = j // 2
        s = "0"*(n-len(s))+s
        ret.append(s)
        #print(i,s)
    return ret

N, M, X = map(int, input().split())
            
buy_list = bit_list(N) #N冊の本を買うか買わないか

book = []

for i in range(M): #本の情報を記録
    A = list(map(int, input().split()))
    book.append(A)
print(book)

ans = []
for j in range(len(buy_list)):#bit探索の1パターン
    AM = [ 0 for _ in range(M)] #M個のアルゴリズムのスキル
    for k in range(N):#本の個数
        for i in range(M):#A[0]はコストのため、M個のアルゴリズムの分をたす
            #print(book[int(buy_list[j][k])][k+1], int(buy_list[j][i]))
            AM[i] += book[int(buy_list[j][k])][i+1]*int(buy_list[j][k]) #jを買う時、iのアルゴリズムの伸び
    ans.append(AM)

print(ans)

for j in range(len(buy_list)):
    flg = 0
    cost = 0
    smallest = 10**10
    for i in range(M):
        cost += int(book[i][0])
        print(ans[j][i])
        if ans[j][i] < X:#一つでもX未満であれば
            flg = 1
            break
    if flg == 1: #次のパターンへ
        continue
    else:
        print(smallest, cost)
        smallest = min(smallest,cost)

print(smallest)



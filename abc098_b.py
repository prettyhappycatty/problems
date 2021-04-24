N = int(input())
S = input()


s = 'a'
start = {}
end = {}
for i in range(26):
    small_s = chr(ord(s)+i)
    flg_s = 0
    flg_e = 0
    for j in range(N):
        if S[j] == small_s and flg_s != 1:
            flg_s = 1
            start[small_s] = j
        
        if S[N-1-j] == small_s and flg_e != 1:
            flg_e = 1
            end[small_s] = N-1-j

        if flg_s == 1 and flg_e ==1:
            break

#print(start, end)

max_cnt = 0
max_i = -1  
for i in range(N):
    cnt = 0
    #print(i,N)
    for j in range(26):
        small_s = chr(ord(s)+j)
        #print(i, small_s)
        if small_s in start.keys() and start[small_s] <= i < end[small_s]:
            #print('cnt++')
            cnt += 1

    if cnt > max_cnt:
        #print(cnt)
        max_cnt = cnt

print(max_cnt)
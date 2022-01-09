def gen_tosasu():
    first = range(1,10)
    sec = range(0,10)
    sa = range(-9,10)

    ans = [i for i in range(1,10)]


    for i in range(len(first)):
        for j in range(len(sa)):
            tmp = str(first[i])
            ssa = sa[j]
            bef = first[i]
            keta = 1
            while -1 < bef+ssa and bef+ssa < 10 and keta < 19:
                tmp += str(bef+ssa)
                bef = bef + ssa
                keta += 1
                ans.append(int(tmp))
    ans.sort()
    #print(ans)
    return ans

X = int(input())

ans = gen_tosasu()

for i in range(len(ans)):
    if ans[i] >= X:
        print(ans[i])
        exit()


                


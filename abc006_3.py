N, M = map(int, input().split())

# j = aka*4+rou*3+oto*2
# i = aka + rou + oto
# j - 2*i = aka*2 + rou 

def main(i, j):

    for aka in range(j//4+1):#赤ちゃん
        rou = j - 2*i - aka*2
        oto = i-(aka+rou)
        if rou >=0 and oto >= 0 and aka*4 + rou*3 + oto*2 == j and aka + rou + oto == i:
            print(oto,rou,aka)
            exit()

    print(-1,-1,-1)

main(N,M)


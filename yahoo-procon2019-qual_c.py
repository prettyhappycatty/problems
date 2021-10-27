K, A, B = list(map(int, input().split()))
 
if B-A <= 2 or K < A:
    # A枚を換金できない場合か、換金することで不利になる場合
    print(K+1)
else:
    count = K - (A-1) #最初1枚持っているので、A-1枚をBに変更したときの操作が減る回数
    if count % 2 == 0: #2の倍数のとき
        print(A + (B-A)*count//2)
    else:
        print(A + (B-A)*(count//2) + 1)
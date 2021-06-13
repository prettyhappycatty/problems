A, B, C = map(int, input().split())


if C % 2 ==0:
    if abs(A) == abs(B):
        print("=")
    elif abs(A) > abs(B):
            print(">")
    else:
        print("<")
else:
    if A * B < 0:#片方マイナス
        #マイナスの方が小さくなる
        if A < 0:
            print("<")
        else:
            print(">")
    elif A < 0 and B < 0:#両方マイナス
        #マイナスの絶対値が大きい方が小さくなる
        if abs(A) == abs(B):
            print("=")
        elif abs(A) < abs(B):
                print(">")
        else:
            print("<")
    elif A*B == 0 and A+B != 0:#どちらかがゼロ
        if A < 0 or B > 0:
            print("<")
        elif B < 0 or A > 0:
            print(">")
    else:#両方プラス
        if abs(A) == abs(B):
            print("=")
        elif abs(A) > abs(B):
                print(">")
        else:
            print("<")


#Cが奇数の場合はABマイナスの場合わけが必要
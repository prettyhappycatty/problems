# 幅優先探索、場合の和をつなげるパターンできるかも

from typing import AnyStr


N = int(input())

ans = 0
#数nについて調べ、末尾に数字を追加した数を再起的に調べる
def dfs(n, use3, use5, use7):
    global ans

    if n > N:
        return

    #3種類そろってたら答えに加算
    if use3 and use5 and use7:
        ans += 1
    
    dfs(10*n + 3, True, use5, use7)
    dfs(10*n + 5, use3, True, use7)
    dfs(10*n + 7, use3, use5, True)

dfs(0, False, False, False)

print(ans)

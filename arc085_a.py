N, M = map(int, input().split())

# 1回にかかる時間 1900*M + 100*(N-M)
# Mケースで、正解する確率　p =　1/(M**2) 

print((1900*M + 100*(N - M)) * 2**M )


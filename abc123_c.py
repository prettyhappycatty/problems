N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

move = [A, B, C, D, E]
mem = [N, 0, 0, 0, 0, 0]

if N % min(move) == 0:
    print( N // min(move)+4)
else:
    print( N // min(move)+5)

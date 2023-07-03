# 16:49 ~17:20

MIN_ROW = 7

N, M = map(int, input().split())

def solution():
    if N == 1 or M == 1:
        print(1)
        return

    if N == 2:
        print(min(int(1 + (M-1) / 2), 4))
        return
    
    if M < MIN_ROW:
        print(min(M, 4))
        return

    print(5 + M - MIN_ROW)
    return

solution()
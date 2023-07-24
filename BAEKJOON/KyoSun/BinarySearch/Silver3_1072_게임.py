# 14:48 ~ 15:21

X, Y = map(int, input().split())

def solution():
    Rate = int(Y*100/X)
    left, right = 0, X
    while left <= right:
        mid = (left+right)//2
        cur_rate = int((mid+Y)*100/(mid+X))
        if cur_rate > Rate:
            right = mid - 1
        else:
            left = mid + 1

    if left > X:
        print(-1)
    else:
        print(left)

solution()
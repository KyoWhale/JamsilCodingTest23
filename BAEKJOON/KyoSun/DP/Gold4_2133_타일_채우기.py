# 17:09 ~ X 17:31 한 칸이 채워지지 않을 때는 포함하는지 질게의 테케 확인했음
# https://blog.naver.com/ajy7424/222608567553

N = int(input())

def solution():
    if N % 2 != 0:
        print(0)
        return

    dp = [0] * 31
    dp[0] = 1
    dp[1] = 0
    dp[2] = 3

    for i in range(4, N+1, 2):
        dp[i] = 3 * dp[i-2]
        for j in range(4, i+1, 2):
            dp[i] += 2 * dp[i-j]

    print(dp[N])

solution()
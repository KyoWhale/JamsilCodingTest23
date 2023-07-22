# 16:18 ~ 17:18 반례 모음집 봄 / 항상 마지막 dp원소가 최대일 거라는 보장이 없음

MAX, CNT = 0, 1

N = int(input())
array = list(map(int, input().split()))

dp = [[array[i], 1] for i in range(N)]
dp[0][MAX] = array[0]
dp[0][CNT] = 1

cur_max = 0
for i in range(N):
    for prev_max, prev_cnt in dp[:i]:
        if prev_max < array[i] and prev_cnt + 1 > dp[i][CNT]:
            dp[i] = [array[i], prev_cnt + 1]

    cur_max = max(cur_max, dp[i][CNT])

print(cur_max)

# 5
# 1 2 3 4 3
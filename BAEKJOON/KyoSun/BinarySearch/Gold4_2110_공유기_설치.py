# 16:02 ~ X 16:51
# 구하려는 목표와 동일하게 이진탐색의 요소가 갭이라는 것을 알았지만,
# 공유기를 설치하는 이중 반복문에서 막혀서 틀림
# 문제의 해결방식을 다르게 했어야함
# 공유기의 개수가 정해져있다는 생각으로 접근했지만, 공유기 개수의 크고작음으로 left, right를 정하는 문제였음

import sys
input = sys.stdin.readline

N, C = map(int, input().split())
houses = []
for i in range(N):
    houses.append(int(input()))
houses.sort()
left = 1
right = houses[-1] - houses[0] # 가장 큰 갭

result = 0
while left <= right:
    mid = (left + right) // 2 # 갭의 절반

    last_router = houses[0]
    router_count = 1

    for i in range(1, N):
        if houses[i] >= last_router + mid: # 마지막 라우터 좌표 + 갭 <= 현재 집의 좌표
            # 문제가 요구하는 것 : 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램
            # 그렇기 때문에 마지막 라우터 좌표 + 갭보다 더 먼 거리의 집에 설치
            last_router = houses[i]
            router_count += 1
    
    if router_count >= C: # 라우터 개수가 더 많으면, 갭이 좁았다는 소리이기에 갭을 늘리려면 left를 키워야함
        left = mid+1
        result = mid
    else:
        right = mid-1

print(result)

# N, C = map(int, input().split())
# routers = [int(input())] # 라우터가 아니고 집임
# for i in range(N-1):
#     routers.append(int(input()))
# routers.sort()

# left = routers[0]
# right = routers[-1]
# while left <= right:
#     gap = (left+right)//C
#     print(gap)

#     plant_cnt = 1
#     plant_idx = 0
#     next_idx = plant_idx + 1
#     while plant_cnt < C and next_idx < N:
#         if routers[next_idx] - routers[plant_idx] < gap:
#             next_idx += 1
#         else:
#             plant_idx = next_idx
#             plant_cnt += 1

#     if routers[-1] - routers[plant_idx] < gap:
#         print("Dec")
#         right = gap - 1
#     elif routers[-1] - routers[plant_idx] > gap:
#         print("Inc")
#         left = gap + 1
#     else:
#         break

# print(gap)
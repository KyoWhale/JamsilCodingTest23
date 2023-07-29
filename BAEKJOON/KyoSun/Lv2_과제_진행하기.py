# 17:43 ~ 18:08

def solution(plans):
    answer = []

    for i in range(len(plans)):
        plans[i][1] = int(plans[i][1][:2]) * 60 + int(plans[i][1][3:])
        plans[i][2] = int(plans[i][2])
    plans.sort(key=lambda x: x[1])

    prev_time = plans[0][1]
    q = []
    for course, cur_time, remain in plans:
        time = cur_time - prev_time
        prev_time = cur_time
        while q and time > 0:
            qcourse, qremain = q.pop()
            if time - qremain >= 0:
                answer.append(qcourse)
                time -= qremain
            else:
                q.append([qcourse, qremain - time])
                break

        q.append([course, remain])

    while q:
        answer.append(q.pop()[0])

    return answer

solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]])
solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]])
solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]])
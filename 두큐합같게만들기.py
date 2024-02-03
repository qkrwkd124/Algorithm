from collections import deque

def solution(queue1, queue2):
    answer = 0

    dq1 = deque(queue1)
    dq2 = deque(queue2)

    sum1 = sum(queue1)
    sum2 = sum(queue2)

    # print(sum1,sum2)
    
    limit = len(queue1) * 3

    taget_number = (sum1 + sum2) // 2

    # print(taget_number)

    # if any(n > taget_number for n in dq1) or any(n > taget_number for n in dq2) :
    #     return -1

    while sum1 != sum2 :
        if sum1 > taget_number :
            val = dq1.popleft()
            dq2.append(val)
            sum1 -= val
            sum2 += val
        else :
            val = dq2.popleft()
            dq1.append(val)
            sum1 += val
            sum2 -= val

        answer += 1

        if answer == limit :
            return -1

    return answer


queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]
# queue1 = [1, 2, 1, 2]
# queue2 = [1, 10, 1, 2]
# queue1 = [1, 1]
# queue2 = [1, 5]

print(solution(queue1,queue2))
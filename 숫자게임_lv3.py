from collections import deque

def solution(A, B):
    answer = 0
    
    sort_A = sorted(A, reverse=True)
    sort_B = sorted(B, reverse=True)

    A_dq = deque(sort_A)
    B_dq = deque(sort_B)
    temp_dq = deque()

    while B_dq :
        if A_dq[0] < B_dq[0] :
            A_dq.popleft()
            B_dq.popleft()
            answer+=1
        else :
            A_dq.popleft()
            B_dq.pop()

    return answer



A = [5,1,3,7]
B = [2,2,6,8]

# A = [2,2,2,2]
# B = [1,1,1,1]

A = [3,1,8,2,5]
B = [10,7,4,1,6]

print(solution(A,B))
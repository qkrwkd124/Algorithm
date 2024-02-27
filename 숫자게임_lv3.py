from collections import deque

def solution(A, B):
    answer = 0
    
    sort_A = sorted(A, reverse=True)
    sort_B = sorted(B, reverse=True)

    B_dq = deque(sort_B)
    temp_dq = deque()

    for A_val in sort_A :
        index = None
        for i,B_val in enumerate(sort_B) :

            if B_val == 0 :
                continue
            if A_val < B_val :
                index = i
            else :
                break
        # print(sort_A)
        # print(sort_B)
        # print(f"{A_val} - {index}")
        
        if index != None:
            sort_B[index] = 0
            answer +=1
        # while B_dq :
        #     B_val = B_dq.popleft()

        #     if A_val < B_val :
        #         temp_dq.append(B_val)
        #     else :
        #         B_dq.appendleft(B_val)
        #         break

        # print(f"{A_val} - {temp_dq}")

        # if temp_dq :
        #     temp_dq.pop()
        #     answer +=1
        #     while temp_dq :
        #         B_dq.appendleft(temp_dq.pop())

    return answer



A = [5,1,3,7]
B = [2,2,6,8]

# A = [2,2,2,2]
# B = [1,1,1,1]

A = [3,1,8,2,5]
B = [10,7,4,1,6]

print(solution(A,B))
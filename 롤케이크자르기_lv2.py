from collections import deque, Counter

def solution(topping):
    answer = 0
    
    A = deque([topping[0]])
    B = deque(topping[1:])

    A_cnt = dict(Counter(A))
    B_cnt = dict(Counter(B))

    # print(B_cnt.items())

    while B :
        
        # print(f"{A} : {B}")

        #print(f"{A_cnt} : {B_cnt}")

        if len(A_cnt) == len(B_cnt) :
            answer +=1
        
        topping_num = B.popleft()
        A_cnt.setdefault(topping_num,0)
        A_cnt[topping_num] += 1

        B_cnt[topping_num] -= 1
        if B_cnt[topping_num] == 0 :
            B_cnt.pop(topping_num)

        # A.append(B.popleft())
    
    return answer


topping = [1, 2, 1, 3, 1, 4, 1, 2]
# topping = [1, 2, 3, 1, 4]

print(solution(topping))
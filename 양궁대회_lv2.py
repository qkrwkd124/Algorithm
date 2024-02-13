import time
import copy

def solution(n, info):
    answer = [-1]

    max_gap = 0
    start = time.time()
    def product(start,ryan_info:list) :
        nonlocal max_gap
        nonlocal answer

        if sum(ryan_info) == n :
            # print(ryan_info)
            # if ryan_info == [0,2,2,0,1,0,0,0,0,0,0]:
                # print(ryan_info)

            apeach_score = 0
            ryan_score = 0
            for i in range(11) :
                # print(f"{i}번 {info[i]} <> {ryan_info[i]}")
                if info[i] == 0 and ryan_info[i] == 0 :
                    continue

                if info[i] < ryan_info[i] :
                    ryan_score += 10-i
                else :
                    apeach_score += 10-i
            
            score_gap = ryan_score - apeach_score
            # print(score_gap)
            if score_gap > 0 :
                if max_gap < score_gap :
                    max_gap = score_gap
                    answer = copy.deepcopy(ryan_info)

                elif max_gap == score_gap :
                    # for i in range(10,-1,-1) :
                    #     if ryan_info[i] > answer[i] :
                    #         answer = copy.deepcopy(ryan_info)
                    #         break
                    for i in range(len(ryan_score)):
                        if answer[i] > 0:
                            max_i_1 = i
                        if ryan_info[i] > 0:
                            max_i_2 = i
                    if max_i_2 > max_i_1:
                        answer = copy.deepcopy(ryan_info)
                            
            
            return
        
        else :
            for i in range(start,11) :

                if info[i] >= ryan_info[i] :
                    ryan_info[i] += 1
                    product(i,ryan_info)
                    ryan_info[i] -= 1

    product(0,[0,0,0,0,0,0,0,0,0,0,0])

    # print(max_gap)
    # print(time.time() - start)

    return answer


n = 5
n = 1
n = 9
# n = 10
info = [2,1,1,1,0,0,0,0,0,0,0]
info = [1,0,0,0,0,0,0,0,0,0,0]
info = [0,0,1,2,0,1,1,1,1,1,1]
# info = 	[0,0,0,0,0,0,0,0,3,4,3]

print(solution(n,info))

# test(info,[1, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0])
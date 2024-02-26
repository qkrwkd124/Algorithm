import math

# 제일 큰값부터 차례대로 -1 처리해서 해결.
# 제일 큰값이 여러개일경우 indexs 리스트에 넣어 n이 허용하는 선까지 -1 처리
def solution(n, works):
    answer = 0
    
    # 내림차순으로 정렬하여 [0] 값이 제일 크게 오게 셋팅
    works = sorted(works,reverse=True)


    while sum(works) > 0 and n != 0:
        max_num = works[0]

        indexs = []

        # works[0] 번째 값이랑 같은 값의 index를 append와 동시에 n-1
        for i in range(0,len(works)) :
            if max_num == works[i] and n > 0 :
                indexs.append(i)
                n -=1
            else :
                break
        
        # 큰값과 같은 값을 가진 index를 처리 
        for idx in indexs :
            works[idx] -= 1

    # print(works)

    answer = sum([num**2 for num in works])

    return answer


works = [4, 3, 3]
# works = [2, 1, 2]
# works = [1,1]
n = 4
# n = 1
# n = 3


print(solution(n,works))
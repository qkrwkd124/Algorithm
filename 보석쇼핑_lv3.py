from collections import deque

def solution(gems):
    answer = []

    gem_length = len(set(gems))

    start = 0

    dq = deque()

    for gem in gems :
        dq.append(gem)

        # print(dq)

        while dq[0] in list(dq)[1:] :
            dq.popleft()
            start +=1

        if len(set(dq)) == gem_length :
            answer.append(start+1)
            answer.append(start+len(dq))
            break
        

    return answer


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
gems = ["AA", "AB", "AC", "AA", "AC"]
gems = ["XYZ", "XYZ", "XYZ"]
gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]

print(solution(gems))
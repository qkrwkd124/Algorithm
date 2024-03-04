from itertools import combinations

def solution(gems):
    answer = []

    # print(len(combinations(gems,4)))

    gemss = gems * 10000
    print(len(gemss))

    cnt = 0

    for result in combinations(gemss,4) :
        cnt+=1
        # print(result)

    print(cnt)


    return answer


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]

print(solution(gems))
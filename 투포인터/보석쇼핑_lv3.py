#투 포인터 알고리즘 사용하여 풀이

def solution(gems):
    answer = []

    #시작,끝 위치
    s,e = 0,0

    #보석 갯수
    gem_length = len(set(gems))

    gem_cnt = dict()

    result = []


    #시작 위치가 작을때 까지 
    while s < len(gems) :

        # 보석 갯수가 같으면
        if len(gem_cnt) == gem_length :

            # 특정보석갯수가 0이 되면은 보석갯수가 같으면서 최소길이를 만족하는 경우
            if gem_cnt[gems[s]] -1 < 1 :

                #결과값에 시작위치,끝위치,거리 삽입
                result.append((s+1,e,e-(s+1)))
                #해당 보석 삭제
                gem_cnt.pop(gems[s])

                #시작위치 하나 올리기
                s+=1
                continue
            
            #시작위치를 하나씩 올려주면서 보석갯수 빼기
            gem_cnt[gems[s]] -=1
            s+=1
        #만약 끝위치가 마지막까지 도달하고 보석갯수가 같지않을때 더이상 만족할수 없으므로 종료
        elif e >= len(gems):
            break

        # 끝 위치를 하나씩 올려주면서 보석 갯수 플러스
        else :
            gem_cnt.setdefault(gems[e],0)
            gem_cnt[gems[e]] += 1
            e +=1

    # print(result)
    result = sorted(result, key=lambda x : (x[2],x[0]))
    # print(result)

    answer.append(result[0][0])
    answer.append(result[0][1])

    return answer


# gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
# gems = ["AA", "AB", "AC", "AA", "AC"]
# gems = ["XYZ", "XYZ", "XYZ"]
# gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
gems = ["EMERALD","RUBY","RUBY","DIA","EMERALD","RUBY","DIA"]

print(solution(gems))
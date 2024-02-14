# 백트래킹을 사용하여 푼 문제

def solution(n, info):
    answer = [-1]  # 최적의 화살 분배를 저장할 변수, 초기값은 라이언이 이길 수 없는 경우를 나타내는 [-1]
    max_diff = -1  # 라이언과 어피치 간의 최대 점수 차이, 초기값은 -1

    # dfs 함수: 현재 인덱스(index), 남은 화살(arrows_left), 라이언 점수(ryan_score), 어피치 점수(apeach_score)를 기반으로 탐색
    def dfs(ryan_info, index, arrows_left, ryan_score, apeach_score):
        nonlocal answer, max_diff

        # 남은 화살이 없을 경우 더 이상 탐색하지 않음
        #if arrows_left < 0:
        #    return

        # 모든 점수를 고려했을 때
        if index > 10:
            # 라이언의 점수가 어피치보다 높은 경우
            if ryan_score > apeach_score:
                diff = ryan_score - apeach_score  # 점수 차이 계산
                # 최대 점수 차이를 갱신
                if diff > max_diff:
                    max_diff = diff
                    answer = ryan_info[:]
                # 최대 점수 차이가 동일한 경우 더 낮은 점수를 많이 맞힌 분배를 선택
                elif diff == max_diff and answer != [-1]:
                    for i in range(10, -1, -1):
                        if ryan_info[i] > answer[i]:
                            answer = ryan_info[:]
                            break
                        elif ryan_info[i] < answer[i]:
                            break
            return

        # 현재 점수를 이기기 위해 어피치보다 1개 더 많은 화살 사용
        if arrows_left > info[index]:
            new_ryan_info = ryan_info[:]
            new_ryan_info[index] = info[index] + 1
            dfs(new_ryan_info, index + 1, arrows_left - new_ryan_info[index], ryan_score + 10 - index, apeach_score)

        # 현재 점수를 포기하고 다음 점수로 넘어감
        if info[index] > 0:
            dfs(ryan_info, index + 1, arrows_left, ryan_score, apeach_score + 10 - index)
        else:
            dfs(ryan_info, index + 1, arrows_left, ryan_score, apeach_score)

    # 초기 화살 분배 상태와 점수를 설정하고 dfs 탐색 시작
    initial_ryan_info = [0] * 11
    dfs(initial_ryan_info, 0, n, 0, 0)

    # 최대 점수 차이가 얻어지지 않은 경우 [-1] 반환
    if max_diff <= 0:
        return [-1]

    # 남은 화살을 모두 0점에 사용
    answer[10] += n - sum(answer)
    return answer


n = 5
# n = 1
# n = 9
# n = 10
info = [2,1,1,1,0,0,0,0,0,0,0]
# info = [1,0,0,0,0,0,0,0,0,0,0]
# info = [0,0,1,2,0,1,1,1,1,1,1]
# info = 	[0,0,0,0,0,0,0,0,3,4,3]

print(solution(n,info))

# test(info,[1, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0])
def solution(triangle):
    answer = 0

    # root가 0번 높이라면 1번 높이부터 시작
    for h in range(1,len(triangle)) :
        # 1번 높이의 값부터 처리 위 높이의 값에서 부터 차례대로 내려가 더했을때 max값을 그 자리에 넣어준다
        for i in range(len(triangle[h])) :

            # 삼각형 제일 왼쪽일 경우
            if i == 0 :
                triangle[h][i] += triangle[h-1][i]
            # 삼각형 제일 오른쪽일 경우
            elif i == len(triangle[h]) -1 :
                triangle[h][i] += triangle[h-1][i-1]
            # 나머지 중간
            else :
                triangle[h][i] += max(triangle[h-1][i-1], triangle[h-1][i])
    
    # print(triangle)
    answer = max(triangle[-1])

    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	

print(solution(triangle))
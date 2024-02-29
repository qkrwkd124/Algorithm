def solution(n, stations, w):
    answer = 0

    length = 1+(w*2) # 기지국 범위

    idx = 0

    # 기지국별 계산
    for i,station in enumerate(stations) :
        
        # 4g 좌,우 거리 계산
        left_num = station - w
        right_num = station + w

        # idx 0 부터 시작
        num = left_num - (idx + 1)

        # 4g기지국 범위가 1번까지 미치면 pass
        if num < 1 :
            idx = right_num

        # idx 부터 left 거리까지 계산
        else :
            div_num = num // length
            remain_num = num % length
            answer += div_num
            if remain_num > 0 :
                answer += 1

            # idx를 right 로 이동
            idx = right_num
    
    # 마지막에 idx 가 n 보다 작으면 마지막까지 처리
    if idx < n :
        num = n - idx
        div_num = num // length
        remain_num = num % length
        answer += div_num
        if remain_num > 0 :
            answer += 1


    return answer


n = 11
stations = [4,7,11]
w = 1

n = 16
stations = 	[9]
w = 2

print(solution(n,stations,w))
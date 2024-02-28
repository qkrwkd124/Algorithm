def solution(routes):
    answer = 0
    
    # 나간시점으로 정렬을 한다.
    sort_routes = sorted(routes, key=lambda x: x[1])

    print(sort_routes)

    camera = None

    for route in sort_routes :

        point_in = route[0]
        point_out = route[1]

        #초기 카메라 셋팅
        if not camera :
            camera = point_out
            answer +=1
            continue


        #범위에 들어가면 pass
        if point_in <= camera and camera <= point_out :
            continue
        
        # 범위에 들어가있지않으면 카메라 한대 더
        else :
            #카메라 지점 갱신
            camera = point_out
            answer +=1

    return answer



routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]	

print(solution(routes))
def solution(n, info):
    answer = []

    cnt =0

    def product(ryan_info:list) :
        nonlocal cnt

        if sum(ryan_info) == n :
            # print(ryan_info)
            cnt += 1
            return
        
        else :
            for i in range(11) :
                ryan_info[i] += 1
                product(ryan_info)
                ryan_info[i] -= 1

    product([0,0,0,0,0,0,0,0,0,0,0])
    print(cnt)

    return answer


n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]

print(solution(n,info))
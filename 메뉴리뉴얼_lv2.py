
def solution(orders, course):
    answer = []

    def combine(start:int, path:list) :
        if len(path) == course_num :
            print(path[:])
            
            sort_path = sorted(path)
            join_path = ''.join(sort_path)

            result.setdefault(join_path,(0,course_num))
            cnt,_ = result[join_path]
            result[join_path] = (cnt+1,course_num)
            
            max_cnt.setdefault(course_num,0)
            if max_cnt[course_num] < cnt+1 :
                max_cnt[course_num] = cnt+1
            
            return 
        else : 
            for i in range(start,len(order)) :
                path.append(order[i])
                combine(i+1,path)
                path.pop()

    # subset = ['A','D']
    # answer = all(elem in orders[3] for elem in subset)
                
    result = {}
    max_cnt = {}

    for order in orders :
        for course_num in course :
            if len(order) < course_num :
                continue
            combine(0,[])

    print(result)
    print(max_cnt)

    for key in result :
        cnt,course_num = result[key]

        


    return answer


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
course = [2,3,4]	

print(solution(orders,course))
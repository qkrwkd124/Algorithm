result = []
check = []
course_max_cnt = []
courses = {}

def combi(start:int, n:int, order:list) :
    global result 
    
    if len(result) == n :
        
    else : 
        for i in range(start,len(order)):
            


def solution(orders, course):
    answer = []

    global check

    # subset = ['A','D']
    # answer = all(elem in orders[3] for elem in subset)
    for order in orders :
        for course_num in course :
            check = [False] * course_num
            if len(order) < course_num :
                continue
            combi(0,course_num, order)
    
    return answer


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

print(solution(orders,course))
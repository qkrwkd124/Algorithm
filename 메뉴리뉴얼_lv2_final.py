from collections import Counter

def solution(orders, course):
    answer = []

    def combine(start:int, words:list) :
        if len(words) == course_num :
            # print(path[:])
            
            sort_words = sorted(words)
            join_word = ''.join(sort_words)

            result.append(join_word)

            return 
        else : 
            for i in range(start,len(order)) :
                words.append(order[i])
                combine(i+1,words)
                words.pop()

    for course_num in course :
        result = []
        for order in orders :
            if len(order) < course_num :
                continue
            combine(0,[])
        
        most_cnt_result = Counter(result).most_common()
        answer += [k for k,v in most_cnt_result if v > 1 and v == most_cnt_result[0][1]]

    answer = sorted(answer)

    return answer


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
# orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
course = [2,3,5]
# course = [2,3,4]

print(solution(orders,course))
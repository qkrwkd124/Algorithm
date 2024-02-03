from collections import Counter

def solution(want, number, discount):
    answer = 0
    want_number = {}

    for i in range(len(want)) :
        want_number[want[i]] = number[i]

    n = 0 
    while n+10 <= len(discount) :
        count = Counter(discount[n:n+10])
        
        #print(n,count)

        if want_number == count :
            answer += 1 
        
        n += 1

    return answer


want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

print(solution(want,number,discount))
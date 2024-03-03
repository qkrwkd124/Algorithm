from itertools import combinations
from itertools import permutations

def solution(user_id, banned_id):
    answer = []

    # for result in combinations(user_id,4) :
    #     print(result)
    # for result in permutations(user_id,4) :
    #     c+=1
    #     # print(result)


    # 순열
    def permutations(path:list) :
        nonlocal answer

        if len(path) == len(banned_id) :
            id_list.append(path[:])
            return
        else:
            for i in range(len(user_id)) :
                if user_id[i] not in path :
                    path.append(user_id[i])
                    permutations(path)
                    path.pop()
 
    def check(users) :
        
        # users와 banned_id 를 순서대로 비교.
        # 순서대로 비교할 수 있는 이유는 순열이라 모든 경우의 수를 적용하기 때문
        for i in range(len(banned_id)) :

            # 둘의 크기가 다르면 False
            if len(users[i]) != len(banned_id[i]) :
                return False
            
            # 문자열 하나씩 비교
            for j in range(len(users[i])) :

                # banned_id 의 문자열이 * 이면 넘어감
                if banned_id[i][j] == '*' :
                    continue
                
                # 두 문자가 안맞으면 False
                if users[i][j] != banned_id[i][j] :
                    return False

        # 다 정상적으로 넘어오면 True        
        return True
    
    id_list = []
    permutations([])

    # print(id_list)

    for users in id_list :

        # "******", "******" 와 같이 중복으로 들어올 수 있는 경우가 있으면, 원소의 순서 상관없이 비교할 수 있는 set 써서 비교
        # ['fradi', 'frodo', 'abc123', 'frodoc']
        # ['fradi', 'frodo', 'frodoc', 'abc123']
        # 두 경우의 수가 있으면, 두개를 set으로 변경하면 똑같다고 판단.
        if check(users) :
            if set(users) not in answer :
                answer.append(set(users))

    return len(answer)


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*rodo", "*rodo", "******"]

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]

print(solution(user_id,banned_id))
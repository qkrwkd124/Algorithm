import math

result = []
number = [1,2,4]
start = 0


def solution(n) :
    global start

    perm_len = 1

    while True :
        # print(f"len : {perm_len}")
        end = start + 3**perm_len
        # print(f"end : {end}")
        if n <= end :
            break

        start = end
        perm_len += 1

    #perm(n,perm_len)

    return perm(n,perm_len)



def perm(n,perm_len) :
    global result
    global start

    if len(result) == perm_len:
        start +=1 

        if start == n  :
            return ''.join(list(map(str,result)))
            
        return
    
    else : 
        for i in range(3) :
            result.append(number[i])
            perm_result = perm(n,perm_len)
            if perm_result :
                return perm_result
            result.pop()


def solution2(n: int) -> str:
    number = [1, 2, 4]
    result = []

    while n > 0:
        n -= 1  # 0부터 시작하는 인덱스 조정
        result.append(number[n % 3])
        n //= 3

    return ''.join(map(str, result[::-1]))  # 역순으로 조정


print(solution(50000000))
#print(solution2(50000000))


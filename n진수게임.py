def to_base_n(num,base) :

    digits = "0123456789ABCDEF"
    result = ""

    while num :
        result = digits[num % base] + result
        num //= base

    return result or "0"

def solution(n, t, m, p):
    answer = ''

    num = 0
    numstr = ""

    while len(numstr) <= t*m :

        #print(f"{num} :  {nstr}")
        numstr += to_base_n(num,n)
        num +=1

    # print(numstr)

    # for order in range(t*m) :
    #     if order % m == p-1 :
    #         answer += numstr[order]
    print(numstr[p-1::m][:t])

    # print(len(answer))
    return numstr[p-1::m][:t]

print(solution(16,16,2,2))

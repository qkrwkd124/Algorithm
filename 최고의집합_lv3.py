
# 각 원소의 곱 이 최대가 되는 n개의 수로 이루어진 집합은, s의 값을 공평하게 n개로 나누어 가질수록 그 곱이 커진다.
# 딱 나누어 떨어지지 않는 나머지 값만큼 +1을 해서 편차를 줄이면 된다.
def solution(n, s):

    # n의 갯수가 크면 원소는 0이 없어 s를 만들방법이 없다.
    if n > s :
        return [-1]

    num = s // n 
    num_mod = s % n 

    # 나눈 값을 공평하게 n개를 가져간다.
    answer = [num] * n

    # 나머지 값을 순서대로 +1을 해준다.
    for i in range(num_mod) :
        answer[i] += 1
    
    # 오름차순으로 정렬
    return sorted(answer)


n = 2
n = 5
# n = 10
# n = 2
# n = 2

s = 9
s = 6
# s = 20
# s = 8
# s = 1

print(solution(n,s))


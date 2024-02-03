def solution(n):
    answer = 0

    number = [0] * 60000
    number[0] = 1
    number[1] = 1

    for i in range(2,60000) :
        number[i] = (number[i-2] + number[i-1]) % 1000000007

    return number[n]


n=4

print(solution(n))
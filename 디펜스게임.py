import heapq


def solution(n,k,enemy) :
    
    if k >= len(enemy) :
        return len(enemy)

    hq = []

    for i in range(len(enemy)) :
        heapq.heappush(hq,enemy[i])
        if len(hq) > k :
            val = heapq.heappop(hq)
            # print(i,val,n)
            if n < val :
                return i
            n -= val

    return len(enemy)

n = 7
# n = 2
k = 3
# k = 4
enemy = [4, 2, 4, 5, 3, 3, 1]
# enemy = [3, 3, 3, 3]

print(solution(n,k,enemy))
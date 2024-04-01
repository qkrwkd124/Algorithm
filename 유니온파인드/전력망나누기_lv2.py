from collections import Counter

def find(parent,x) :
    if parent[x] != x :
        parent[x] = find(parent,parent[x])
    
    return parent[x]

def union(parent,a,b) :

    pa = find(parent,a)
    pb = find(parent,b)

    if pa < pb  :
        parent[pb] = pa
    else :
        parent[pa] = pb


def solution(n, wires):

    answer = float('inf') # infinite 값

    for i in range(len(wires)) :
        parent = [i for i in range(n+1)]
        for j,wire in enumerate(wires) :
            if i == j :
                continue

            union(parent,wire[0],wire[1])

        #모든 부모값을 최상위부모값으로 변환.
        for i in range(1,n+1) :
            find(parent,i)
    
        # print(parent)
        cnt = Counter(parent)
        cnt.pop(0)
        # print(cnt)
        keys = list(cnt.keys())

        sum_val = abs(cnt[keys[0]] - cnt[keys[1]])
        answer = min(answer,sum_val)


    return answer

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]] 

# n = 4
# wires = [[1,2],[2,3],[3,4]]

# n = 7
# wires = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]

print(solution(n,wires))

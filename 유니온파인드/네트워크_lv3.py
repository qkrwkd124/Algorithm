from collections import Counter

def find(parent:list, x:int) :
    if parent[x] != x :
        parent[x] = find(parent,parent[x])
    
    return parent[x]

def union(parent:list, a:int, b:int) :

    root_a = find(parent,a)
    root_b = find(parent,b)

    if root_a < root_b :
        parent[root_b] = root_a
    else :
        parent[root_a] = root_b


def solution(n, computers):
    answer = 0

    parent = [i for i in range(n)]

    for a in range(n) :
        for b in range(n) :
            if a == b :
                continue

            if computers[a][b] == 1 :
                union(parent,a,b)
                
        print(parent)

    
    # print(Counter(parent).values())

    # for i in range(n):
    #     find(parent, i)

    # print(parent)
    
    answer = len(set(parent))


    return answer


n = 3
n = 5
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
computers = [[1, 1, 1, 0, 0], [1, 1, 1, 0, 0], [1, 1, 1, 0, 0],[0, 0, 0, 1, 1], [0,0,0,1,1]]

#예외상황..
n = 5
computers= [[1, 0, 0, 0, 1], [0, 1, 1, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 1, 1], [1, 0, 0, 1, 1]]



print(solution(n,computers))
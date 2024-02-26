from collections import deque

#위 아래
dx = [0,1]
dy = [1,0]

def solution(m, n, puddles):
    answer = 0

    min_cnt = ''
    
    dq = deque()
    dq.append((1,1,0))

    def bfs (dq:deque) :

        nonlocal answer
        nonlocal min_cnt

        while dq :
            x,y,cnt = dq.popleft()

            if min_cnt :
                if cnt > min_cnt :
                    continue
            
            if x == m and y == n :
                min_cnt = cnt
                answer +=1
                continue

            for i in range(2) :
                nx = x+dx[i]
                ny = y+dy[i]

                if nx < 1 or ny < 1 or nx >m or ny >n :
                    continue

                if [nx,ny] in puddles :
                    continue

                dq.append((nx,ny,cnt+1))

    bfs(dq)
        
    return answer


m = 4
n = 3 
puddles = [[2, 2]]

print(solution(m,n,puddles))




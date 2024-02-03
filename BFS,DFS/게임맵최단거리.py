from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def solution(maps):
    answer = -1
    n = len(maps)
    m = len(maps[0])

    if maps[n-2][m-1] == 0 and maps[n-1][m-2] == 0 :
        return -1

    visited = [[False]*len(maps[i]) for i in range(len(maps))]

    start = (0,0,1)
    visited[0][0] = True

    dq = deque()
    dq.append(start)

    while dq :
        x,y,cnt = dq.popleft()

        #print(f"{x},{y}:{cnt}")

        if x == n-1 and y == m-1 :
            answer = cnt
            break

        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]

            if nx >= n or ny >= m or nx < 0 or ny < 0 :
                continue

            if maps[nx][ny] == 1 and not visited[nx][ny] :
                dq.append((nx,ny,cnt+1))
                visited[nx][ny] = True
        
    return answer


maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]

print(solution(maps))
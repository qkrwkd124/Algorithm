from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def solution(board):
    answer = -1

    #visited = [[False]*len(i) for i in board]
    visited = []
    # gx,gy = None,None

    for i,ival in enumerate(board) :
        visited.append( [False]*len(ival) )
        for j,jval in enumerate(ival) :
                           
            if jval == 'G' :
                gx,gy = i,j
            if jval == 'R' :
                rx,ry = i,j

    # print(visited)
    # print(rx,ry)
    # print(gx,gy)
    dq = deque()

    dq.append((rx,ry,0))
    visited[rx][ry] = True

    while dq :

        # print(dq)
        x,y,cnt = dq.popleft()

        # print(x,y,cnt)
        if gx == x and gy == y :
            answer = cnt
            break

        for i in range(4) :
            sx = x
            sy = y 
            while True :
                nx = sx+dx[i]
                ny = sy+dy[i]

                if nx < 0 or ny < 0 or nx >= len(board) or ny >= len(board[0]) :
                    break
                
                if board[nx][ny] == 'D' :
                    break

                sx = nx
                sy = ny

            if not visited[sx][sy] :
                visited[sx][sy] = True
                dq.append((sx,sy,cnt+1))

    return answer


board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
board = [".D.R", "....", ".G..", "...D"]

print(solution(board))
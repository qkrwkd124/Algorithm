from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(dq:deque, place:list, visited:list) :

    # dq = deque((x,y,0))
    # visited[x][y] = True

    #print(dq)

    while dq :
        print(dq)
        x,y,cnt = dq.popleft()

        if cnt > 1 and place[x][y] == 'P' :
            return False

        if cnt > 2 :
            continue

        
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            # print(nx,ny)

            if nx < 0 or ny < 0 or nx >= 5 or ny >=5 :
                continue

            # if place[nx][ny] == 'P' :
            #     print(nx,ny)
            #     return False
            
            if not visited[nx][ny] and place[nx][ny] == 'O' :
                dq.append((nx,ny,cnt+1))

    
    return True

def solution(places):
    answer = []


    for place in places :

        safe = True
            
        def is_safe(places:list) :
            dq = deque()

            for x,POX in enumerate(place) :
                for y,val in enumerate(POX) :
                    if val == 'P' :
                        visited = [[False]*5 for _ in range(5)]
                        dq.append((x,y,0))
                        visited[x][y] = True
                        safe = bfs(dq,place,visited)

                        if not safe :
                            return False
            return True
            # is_safe = bfs(dq,place,visited)

            # if is_safe :
            #     answer.append(1)
            # else :
            #     answer.append(0)

            # break
        safe = is_safe(place)
        print(safe)

        if safe :
            answer.append(1)
        else :
            answer.append(0)

        # break

    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]
          ,["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"]
          ,["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"]
          ,["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"]
          ,["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]


print(solution(places))
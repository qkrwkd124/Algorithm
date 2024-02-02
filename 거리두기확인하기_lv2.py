from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(dq:deque, place:list, visited:list) :

    while dq :
        # print(dq)
        x,y,cnt = dq.popleft()

        # 이동횟수가 3번 이상이면은 그만
        if cnt > 2 :
            continue

        # 한번 이동하고 사람을 만나면은 안전하지 않다고 판단
        if cnt > 0 and place[x][y] == 'P' :
            return False

        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or ny < 0 or nx >= 5 or ny >=5 :
                continue

            if visited[nx][ny] or place[nx][ny] == 'X' :
                continue

            dq.append((nx,ny,cnt+1))
            visited[nx][ny] = True
    
    return True

def solution(places):
    answer = []

    for place in places :

        safe = True
            
        def is_safe(places:list) :
            dq = deque()

            for x,POX in enumerate(place) :
                for y,val in enumerate(POX) :
                    # 루프를 돌려 사람일 경우 최대 2번의 이동안에 사람을 만날경우 안전하지 않다고 판단하고 return False
                    # 각 대기실마다 사람마다 작동
                    if val == 'P' :
                        visited = [[False]*5 for _ in range(5)]
                        dq.append((x,y,0))
                        visited[x][y] = True
                        safe = bfs(dq,place,visited)

                        if not safe :
                            return False
                        
            return True
        
        safe = is_safe(place)
        # print(safe)

        if safe :
            answer.append(1)
        else :
            answer.append(0)

    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]
          ,["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"]
          ,["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"]
          ,["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"]
          ,["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]


print(solution(places))
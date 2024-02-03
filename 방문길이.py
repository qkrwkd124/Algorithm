"""
프로그래머스 2레벨 문제
"""
def solution(dirs):
    answer = 0

    visited = {}
    x,y = 0,0

    for order in dirs :
        if order == 'U' :
            nx = x
            ny = y+1
        elif order == 'D' :
            nx = x
            ny = y-1
        elif order == 'R' :
            nx = x+1
            ny = y
        elif order == 'L' :
            nx = x-1
            ny = y

        print(f"{x},{y} -> {nx},{ny}")

        if nx > 5 or ny > 5 or nx < -5 or ny < -5 :
            continue

        check_visit = f"{x}{y}{nx}{ny}"
        
        if check_visit in visited :
            x,y = nx,ny
            continue

        visited[check_visit] = 1
        visited[f"{nx}{ny}{x}{y}"] = 1
        answer+=1

        x,y = nx,ny

    return len(visited) // 2


dirs = "ULURRDLLU"
dirs = "LULLLLLLU"
# dirs = "URDLURDLDLURULDRR"

print(solution(dirs))
def solution(k, dungeons):

    answer = -1
    visited = [False] * len(dungeons)

    def adventure(k,cnt) :
        nonlocal answer
        nonlocal dungeons
        nonlocal visited

        if answer < cnt :
            answer = cnt
        
        for idx in range(len(dungeons)) :
            minp = dungeons[idx][0]
            miusp = dungeons[idx][1]

            if not visited[idx] and k >= minp :
                visited[idx] = True
                adventure(k-miusp,cnt+1)
                visited[idx] = False
            
    adventure(k,0)

    return answer

k = 80
dungeons = [[80,20],[50,40],[30,10]]

print(solution(k,dungeons))
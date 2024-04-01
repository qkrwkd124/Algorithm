from collections import deque

def down(area,x,y,n,value) :
    for i in range(n) :
        area[x+i][y] = value+i

    return x+i,y+1,value+i+1

def right(area,x,y,n,value):
    for i in range(n) :
        area[x][y+i] = value+i

    return x-1,y+i-1,value+i+1

def up(area,x,y,n,value):
    for i in range(n) :
        area[x-i][y-i] = value+i

    return x-i+1,y-i,value+i+1
    

def solution(n):
    answer = []

    area = [[0]*n for _ in range(n)]
    x,y,value = 0,0,1
    check = 0
    ln = n

    print(area)

    while ln > 0 :

        if check % 3 == 0 : 
            x,y,value = down(area,x,y,ln,value)
            ln -= 1
        elif check % 3 == 1 :
            x,y,value = right(area,x,y,ln,value)
            ln -= 1
        elif check % 3 == 2 :
            x,y,value = up(area,x,y,ln,value)
            ln -= 1

        check +=1

    # for i in range(n) :
    #     print(area[i])
    
    for i in range(n) :
        for j in range(n) :
            if area[i][j] > 0 :
                answer.append(area[i][j])

    return answer

n = 5
n = 6
n = 7 

print(solution(n))

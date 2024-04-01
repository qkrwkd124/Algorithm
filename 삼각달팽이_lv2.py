from collections import deque

dx = [1,0,-1]
dy = [0,1,-1]

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
    value = 1

    print(area)

    while n > 1 :
        x,y,value = down(area,0,0,n,value)
        n -= 1
        x,y,value = right(area,x,y,n,value)
        n -= 1
        x,y,value = up(area,x,y,n,value)
        n -= 1

    for i in range(n) :
        print(area[i])
    

    





    return answer

n = 5
n = 6

print(solution(n))

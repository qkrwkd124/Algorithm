dx = [1,0,1]
dy = [0,1,1]

def delete(m,n,board) :
    delete_check = False
    delete_list = set()

    for x in range(m):
        for y in range(n) :

            if board[x][y] == '' :
                continue

            friend = board[x][y]
            cnt = 0

            for k in range(3) :
                nx = x+dx[k]
                ny = y+dy[k]

                if nx < 0 or ny < 0 or nx >= m or ny >= n :
                    break

                if board[nx][ny] == friend :
                    cnt += 1

            if cnt == 3 :
                delete_list.add((x,y))
                delete_list.add((x+1,y))
                delete_list.add((x,y+1))
                delete_list.add((x+1,y+1))

    
    for x,y in delete_list :
        delete_check = True
        board[x][y] = ''

    return len(delete_list),delete_check,board

def down(m,n,board) :

    for x in range(m-2,-1,-1) :
        for y in range(n) :
            
            friend = board[x][y]

            if friend == '' :
                continue

            ox = x
            oy = y

            while True :
                nx = ox+1
                ny = oy

                if nx >= m or board[nx][ny] != '':
                    break

                ox = nx
                oy = ny

            board[x][y] = ''
            board[ox][oy] = friend
    
    return board

def solution(m, n, board):
    answer = 0

    board = [list(friends) for friends in board]
    
    while True :
        cnt,check,board = delete(m,n,board)
        answer += cnt

        if not check :
            break

        # print(board)

        board = down(m,n,board)

        # print(board)

    return answer


m = 4
# m = 6
n = 5
# n =6 
board =    ["CCBDE", "AAADE", "AAABF", "CCBBF"]
# board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

print(solution(m,n,board))
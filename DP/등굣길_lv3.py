
def solution(m, n, puddles):
    map = [[0]*(m+1) for _ in range(n+1)]

    map[1][1] = 1

    #1,1 부터 시작    
    for i in range(1,n+1) :
        for j in range(1,m+1) :

            if i == 1 and j == 1 :
                continue
            
            #puddles 는 m,n 으로 주어지기 때문에 n,m인 맵에서는 거꾸로 생각해야한다.
            #물웅덩이면은 지나가기
            if [j,i] in puddles :
                continue
            
            # 위,왼 값 플러스
            map[i][j] = (map[i-1][j] + map[i][j-1]) % 1000000007

    # for row in map :
    #     print(row)
        
    return map[n][m]


m = 4
n = 3 
puddles = [[2,1],[2, 2],[2,3],[2,4],]

print(solution(m,n,puddles))




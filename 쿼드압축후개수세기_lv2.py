def solution(arr):
    answer = [0,0]

    length = len(arr)

    def compress(a,b,l) :
        start = arr[a][b]

        # print('go')
        # print(f"{a},{a+l}")
        # print(f"{b},{b+l}")

        # 0,0 부터 시작. 
        # i:range(0,8) j:range(0,8)
        for i in range(a,a+l) :
            for j in range(b,b+l) :
                
                # 기준숫자보다 다르면 쿼드트리 방식
                if start != arr[i][j] :
                    l = l//2
                    compress(a,b,l) # 좌상단
                    compress(a,b+l,l) # 우상단 
                    compress(a+l,b,l) # 좌하단
                    compress(a+l,b+l,l) # 우하단

                    return

        
        answer[start] +=1
        # print(answer)

    compress(0,0,length)


    return answer

# i:range(0,8) j:range(0,8)
# i:range(0,4) j:ragne(0,4) | i:range(0,4) j:range(4,8) | i:range(4,8) j:range(0,4) | i:range(4,8) j:range(4,8)


arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
# arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]

print(solution(arr))
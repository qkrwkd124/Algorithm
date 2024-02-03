import heapq

def solution(scoville, K):
    answer = 0

    min_heap = []

    for scovil in scoville :
        heapq.heappush(min_heap,scovil)
    

    while len(min_heap) > 0 :
        if min_heap[0] >= K :
            return answer
        
        if len(min_heap) > 1 :
            first_min = heapq.heappop(min_heap)
            second_min = heapq.heappop(min_heap)

            heapq.heappush(min_heap,first_min + (second_min*2))
            answer += 1 
        else :
            return -1
        #print(min_heap)

    #return -1


scoville = [1, 2, 3, 9, 10, 12]
K = 30

print(solution(scoville=scoville,K=K))
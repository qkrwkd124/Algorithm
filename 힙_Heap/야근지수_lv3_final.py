from heapq import heapify, heappop, heappush


#정렬을 통해 푼 문제를 heap으로 풀어본 풀이
def solution(n,works) :
	answer = 0

	# 파이썬의 힙이 기본적으로 최소 힙(min heap)이기 때문에, 작업량이 많은 것을 우선적으로 처리하기 위해 최대 힙(max heap)으로 사용하기 위한
	heapify(works:=[-i for i in works])

	# print(works)

	# while abs(sum(works)) > 0 and n != 0 : 효율성테스트 에서 불합. => 실행할때마다 sum을 해서 효율성에서 떨어진듯.
	# 	heappush(works,heappop(works)+1)
	# 	n -=1

	#sum(work) 값이랑 n 값중 작은값만큼 for문 실행.
	for i in range(min(n, abs(sum(works)))):
		heappush(works, heappop(works)+1)
	
	answer = sum([num**2 for num in works])


	return answer


works = [4, 3, 3]
works = [2, 1, 2]
works = [1,1]
n = 4
n = 1
n = 3


print(solution(n,works))
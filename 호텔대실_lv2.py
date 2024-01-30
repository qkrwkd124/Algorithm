from heapq import heappush, heappop

def time_to_convert(time) :
    stime:str = time[0]
    etime:str = time[1]

    shour, sminute = tuple(map(int,stime.split(':')))
    ehour, eminute = tuple(map(int,etime.split(':')))
    
    return shour*60 + sminute, ehour*60 + eminute + 10
	
def solution(book_time):
    
    # check_in 순서로 정렬
    book_time = sorted(book_time, key=lambda x:x[0])
    print(book_time)

    room = []

    # 정렬순서대로 최소힙에 check_out push
    # 최소 check_out 시간 보다 check_in 시간이 나중에 들어오면 pop
    #  => 최소 check_out 시간이 check_in 보다 작으면 이제 더이상 객실 이용을 안하면 되기때문에 pop 을 함
    for time in book_time :
        check_in, check_out = time_to_convert(time)
        if room and room[0] <= check_in :
            heappop(room)
        heappush(room,check_out)
        
    return len(room)

book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"],["18:30","19:00"],["00:00","23:59"]]
# book_time = [["09:10", "10:10"], ["10:20", "12:20"]]
# book_time = [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]
#book_time = [["00:00", "01:50"], ["02:00", "03:30"], ["03:30", "04:30"], ["22:50", "23:59"]]
print(solution(book_time))
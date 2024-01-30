
def time_to_minute(time) :
    stime:str = time[0]
    etime:str = time[1]

    shour, sminute = tuple(map(int,stime.split(':')))
    ehour, eminute = tuple(map(int,etime.split(':')))
    
    return shour*60 + sminute, ehour*60 + eminute + 10
	

def solution(book_time):
    answer = 0
    
    cnt = 1
    room = [cnt]
    
    for i,time in enumerate(book_time[1:]) :
        nsminute, neminute = time_to_minute(time)
        #print(nminute, nminute)

        check = False

        for j in range(len(room)) :
            sminute, eminute = time_to_minute(book_time[j])
            print(f"{nsminute}-{neminute} , {sminute},{eminute}")
            if nsminute >= eminute or neminute <= sminute :
                room.append(room[j])
                check = True
                break
        
        if not check :
            cnt+=1
            room.append(cnt)

        
    return max(room)

# book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"],["18:30","19:00"]]
# book_time = [["09:10", "10:10"], ["10:20", "12:20"]]
# book_time = [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]
book_time = [["00:00", "01:50"], ["02:00", "03:30"], ["03:30", "04:30"], ["22:50", "23:59"]]
print(solution(book_time))
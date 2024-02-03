import math

def time_to_minutes(time:str) :
    hour,minutes = map(int,time.split(':'))
    return (hour*60) + minutes


def solution(fees, records):
    answer = []

    result = {}
    times = {}

    for record in records :
        time,carnum,stats = record.split(' ')
        
        if stats == "IN" :
            times[carnum] = time_to_minutes(time)
        else :
            in_time_minute = times[carnum]
            out_time_minute = time_to_minutes(time)
            
            result.setdefault(carnum,0)
            result[carnum] += (out_time_minute - in_time_minute)

            times.pop(carnum)

    if times :
        for carnum in times :
            in_time_minute = times[carnum]
            out_time_minute = time_to_minutes("23:59")
            result.setdefault(carnum,0)
            result[carnum] += (out_time_minute - in_time_minute)

    keys = sorted(result.keys())
    #print(result)
    for key in keys :
        duration = result[key]
        if duration <= fees[0] :
            answer.append(fees[1])
        else :
            answer.append( fees[1] + (math.ceil((duration-fees[0])/fees[2])*fees[3]) )

    return answer


fees = [180, 5000, 10, 600]
fees = [120, 0, 60, 591]
fees = [1, 461, 1, 10]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
records =["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
records = ["00:00 1234 IN"]

print(solution(fees=fees, records=records))


# x = (18*60)+59
# y = (23*60)+00

# h = (y-x) // 60
# m = (y-x) % 60
# print(f"{h}:{m}")

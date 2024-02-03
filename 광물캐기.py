diamond_fat = {
    "diamond" : 1,
    "iron" : 1,
    "stone" : 1
}
iron_fat ={
    "diamond" : 5,
    "iron" : 1,
    "stone" : 1
}
ston_fat ={
    "diamond" : 25,
    "iron" : 5,
    "stone" : 1
}

def solution(picks, minerals):
    answer = 0

    dia = []
    iron = []
    stone = []

    # 캘수있는 곡괭이 수가 총 미네랄갯수보다 많으면은 미네랄을 다 캘수있어서 length를 미네랄 갯수만큼
    # 아니면은 곡괭이로 캘수있는 만큼만 커버.
    if sum(picks) * 5 >= len(minerals) :
        mineral_length = len(minerals)
    else : 
        mineral_length = sum(picks)*5

    # 미네랄을 5개씩 묶어 다이아몬드,철,돌 각각 피로도를 계산한다.
    for s in range(0,mineral_length,5) :
        dia.append(sum([diamond_fat[mineral] for mineral in minerals[s:s+5]]))
        iron.append(sum([iron_fat[mineral] for mineral in minerals[s:s+5]]))
        stone.append(sum([ston_fat[mineral] for mineral in minerals[s:s+5]]))

    # stone 을 기준으로 정렬을 한다.       
    sort_zip  = sorted(zip(dia,iron,stone),key=lambda x:x[2], reverse=True)
    dia[:],iron[:],stone[:] = zip(*sort_zip)
    print(dia,iron,stone)


    # 정렬된 기준으로 가장 피로도가 높은순으로 정리가 되어 다이아 곡괭이부터 소비하면된다.
    for i in range(len(stone)) :

        if picks[0] > 0 :
            answer += dia[i]
            picks[0] -= 1
        
        elif picks[1] > 0 :
            answer += iron[i]
            picks[1] -= 1

        elif picks[2] > 0 :
            answer += stone[i]
            picks[2] -= 1

    return answer


picks = [1, 3, 2]
minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]

# picks = [0, 1, 1]
# minerals =["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]

# picks = [1,1,1]
# minerals =["stone", "stone", "stone", "stone", "stone", "iron", "iron", "iron", "iron", "iron","stone", "stone", "stone", "stone", "stone"]

print(solution(picks,minerals))
# dia = [5,3]
# iron = [17,7]
# stone = [85,31]

# picks = [0, 1, 1]
# minerals = ["iron", "iron", "iron", "iron", "iron","diamond", "diamond", "diamond", "diamond", "diamond", "diamond", "iron"]

# dia = [5,5,5]
# iron = [5,25,10] # 2
# stone = [25,125,45] # 2

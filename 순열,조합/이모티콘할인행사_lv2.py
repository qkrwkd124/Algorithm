def solution(users, emoticons):
    answer = [0,0]
    
    def permute(percents:list) :
        nonlocal answer 

        if len(percents) == len(emoticons) :
            
            result = [0,0]

            for user in users :
                rate = user[0]
                price = user[1]
                user_price_sum = 0

                for i,emoticon_price in enumerate(emoticons) :
                    if rate <= percents[i] :
                        user_price_sum += int(emoticon_price * (100-percents[i]) / 100)

                if price <= user_price_sum :
                    result[0] = result[0] + 1
                else :
                    result[1] = result[1] + user_price_sum

            # 아래의 수식을 max 함수로 가능.
            # if answer[0] < result[0] : 
            #     answer[0] = result[0]
            #     answer[1] = result[1]
            # elif answer[0] == result[0] :
            #     if answer[1] < result[1] :
            #         answer[0] = result[0]
            #         answer[1] = result[1]
            
            # 리스트로 비교가능, 리스트순서대로 max값 비교해서 넣음
            answer = max(answer,result)


            return
        else :
            for percent in [10,20,30,40] :
                percents.append(percent)
                permute(percents)
                percents.pop()
    

    permute([])

    return answer


users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]    
emoticons = [1300, 1500, 1600, 4900]


print(solution(users,emoticons))
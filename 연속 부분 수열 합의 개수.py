def solution(elements):
    
    result = set()
    elements_len = len(elements)
    for start in range(elements_len) :
        for end in range(1,elements_len+1) :
            
            if start+end > len(elements) :
                result.add(( sum(elements[start:]) + sum(elements[:(start+end)%len(elements)]) ))
            else :
                result.add(sum(elements[start:start+end]))   
            # sum = 
            # #print(start,end)
            # for idx in range(start,start+end) :
            #     idx = idx % elements_len
            #     sum = elements[idx] + sum

            #print(sum)

    #print(result)
    return len(result)


elements = [7,9,1,1,4]
print(solution(elements))
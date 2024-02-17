def solution(v) :

    answer = []

    x = []
    y = []

    for i in v :
        vx = i[0]
        vy = i[1]

        if vx in x :
            x.remove(vx)
        else :
            x.append(vx)
        
        if vy in y :
            y.remove(vy)
        else :
            y.append(vy)

    answer = x+y
    return answer 


v = [[1,4],[3,4],[3,10]]
print(solution(v))
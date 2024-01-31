import re

def operator_result(oper:str,num1:int,num2:int) :
    if oper == '+' :
        return num1+num2
    elif oper == '-' :
        return num1-num2
    elif oper == '*' :
        return num1*num2

def solution(expression):
    answer = 0
    
    num_pattern = r'\d+'
    num_match = re.findall(num_pattern,expression)
    # print(num_match)

    oper_pattern = r'[\-\+\*]+'
    oper_match = re.findall(oper_pattern,expression)
    # print(oper_match)

    def permute_unique(path:list) :
        nonlocal answer
        if len(path) == 3 :
            
            numbers = num_match[:]
            operators = oper_match[:]

            for path_oper in path :
                while path_oper in operators :
                    for i,operator in enumerate(operators) :
                        if path_oper == operator :
                            numbers[i] = operator_result(operator,int(numbers[i]),int(numbers[i+1]))
                            numbers.pop(i+1)
                            operators.pop(i)
                            break

            # print(path)
            # print(abs(numbers[0]))

            answer = max(answer,abs(numbers[0]))

            return
        else :
            for operator in ['+','-','*'] :
                if operator in path :
                    continue
                path.append(operator)
                permute_unique(path)
                path.pop()

    permute_unique([])

    return answer


expression = "100-200*300-500+20"
expression = "50*6-3*2"
print(solution(expression=expression))
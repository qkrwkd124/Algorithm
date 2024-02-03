# result = []
# check = []
# answer = 0

# def solution(number, k):

#     global check
    
#     check = [False]*len(number)

#     combi(0,k,number)

#     return str(answer)

# def combi(start,k,number) :

#     global check
#     global result
#     global answer

#     if len(result) == k:
        
#         string = ''.join(number[i] for i in range(len(number)) if i not in set(result))

#         if answer < int(string) :
#             answer = int(string)

#         return 
#     else : 

#         for i in range(start,len(number)) :
#             if not check[i] :
#                 check[i] = True
#                 result.append(i)
#                 combi(i,k,number)
#                 result.pop()
#                 check[i] = False


def solution(number, k):

    stack = []
    top = 0
    cnt = 0
    stack.append(int(number[0]))
    length = len(number) - k 

    for i in range(1,len(number)) :
        num = int(number[i])
        # print(num)
        
        while stack :
            if stack[top] < num and cnt != k:
                stack.pop()
                top -=1
                cnt +=1
            else : 
                break

        stack.append(num)
        top+=1

    # print(stack)

    return ''.join(list(map(str,stack[:length])))

# numbers = ["1924","1231234","4177252841","1717543"]
# ks = [2,3,4,3]

numbers = ["1717543"]
ks = [3]

for number, k in zip(numbers,ks) :
    print(solution(number,k))
def str_separate(p) :
	
    val = 0
    check = True

    for i,s in enumerate(p) :
        if s == '(' :
            val += 1
        else :
            val -= 1

        if val < 0 : # val 이 0보다 작아지면 ')' 값이 먼저 들어왔다는 뜻, 그러므로 올바른 괄호가 될 수 없음.
            check = False

        if val == 0 : # 균형잡힌 괄호면 리턴
            return check,p[:i+1],p[i+1:]
	# left_p=0
	# right_p=0

	# for i,s in enumerate(p) :
	# 	if s == '(' :
	# 		right_p +=1
	# 	elif s == ')' :
	# 		left_p +=1

	# 	if left_p == right_p :
	# 		return p[:i+1], p[i+1:]
	
# def is_collect(p) : 
# 	stack = []

# 	for s in p :
# 		if s == '(' :
# 			stack.append('(')
# 		elif s == ')' :
# 			if not stack :
# 				return False
# 			stack.pop()

# 	if not stack :
# 		return True
# 	else :
# 		return False

def solution(p):

	if p == '' :
		return ''

	check,u,v = str_separate(p)

	if check : # 올바른 괄호면
		return u + solution(v)
	else :
		return '(' + solution(v) + ')' + ''.join(list(map(lambda s: '(' if s == ')' else ')', u[1:-1]))) # map(함수,iterable객체) iterable 값을 lambda 함수로 거꾸로 바꿔줌
		# plus_v = '(' + solution(v) + ')'
		# reverse_u = ''
		# for s in u[1:-1] :
		# 	if s == ')' :
		# 		reverse_u += '('
		# 	elif s == '(' :
		# 		reverse_u += ')'
		# return plus_v + reverse_u



p="()))((()"
p=")("
p="(()())()"

print(solution(p))
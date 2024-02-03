
words = ['A', 'E', 'I', 'O', 'U']
answer = 0
cnt = 0

class FoundWord(Exception) :
    pass

def dfs(word, cur_word) :
    global cnt
    cnt += 1
    #print(cnt,cur_word)

    if word == cur_word :
        global answer
        answer = cnt
        raise FoundWord()

    if len(cur_word) >= 5:
        return

    for i,val in enumerate(words) :
        dfs(word,cur_word+val)
    

def solution(word):
    try :
        for i,val in enumerate(words) :
            dfs(word,val)
    except FoundWord :
        pass
    
    return answer

word = "AAAAE"
word = "AAAE"
word = "I"
word = "EIO"
print(solution(word))

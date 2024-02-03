def solution(files):
    answer = []

    hnt = {}

    for file in files :
        head = ''
        number = ''
        tail = ''
        for word in file :

            if not word.isdigit() : #문자열인 경우
                if number :
                    tail += word
                else :
                    head += word
            else : # 숫자일 경우
                if not tail and len(number) < 5 :
                    number += word
                else :
                    tail += word

        hnt[file] = (head.lower(),int(number))
    

    print(hnt)

    answer = sorted(files, key=lambda x:(hnt[x][0],hnt[x][1]))

    return answer


files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG","AMG00002b00.png","amg0002a00.png"]
#files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
#files = ["MUZI01.zip","muzi1.png"]
print(solution(files))
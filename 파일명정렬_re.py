import re

def solution(files):
    answer = []

    hnt = {}
    pattern = r"([a-zA-Z\-\.\ ]+)(\d{1,5})(.*)"

    for file in files :
        
        match = re.match(pattern,file)
        # print(match.group(1))
        # print(match.group(2))
        # print(match.group(3))
        hnt[file] = (match.group(1).lower(),int(match.group(2)))
    

    print(hnt)

    answer = sorted(files, key=lambda x:(hnt[x][0],hnt[x][1]))

    return answer


files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG","AMG00002b00.png","amg0002a00.png"]
#files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
#files = ["MUZI01.zip","muzi1.png"]
print(solution(files))
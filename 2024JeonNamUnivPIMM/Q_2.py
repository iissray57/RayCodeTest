def solution(str):
    songs = {}
    answer = []
    data = str.split("\r\n")
    cnt = data[0].split(" ")
    
    for i in range(1, len(data)) :
        if i <= int(cnt[0]):
            song = data[i].split(" ")
            songs[song[1]] = ''.join(song[2:5])
        else :
            test = data[i].replace(" ", "")
            matchCnt = 0
            matchSong = ""
            for song in songs :
                if matchCnt == 2 :
                    answer.append("?")
                    break
                if test == songs[song] :
                    matchCnt += 1
                    matchSong = song

            if matchCnt == 1 :
                answer.append(matchSong)
            else :
                answer.append("!")
    print(answer)

# 4 4\r\n11 TwinkleStar C C G G A A G\r\n8 Marigold E D E F E E D\r\n23 DoYouWannaBuildASnowMan C C C G C E D\r\n12 Cprogramming C C C C C C C\r\nE D E\r\nC G G\r\nC C C\r\nC C G

# str = input()
# songs = {}
# answer = []
# data = str.split("\\r\\n")
# cnt = data[0].split(" ")

# for i in range(1, len(data)) :
#     if i <= int(cnt[0]):
#         song = data[i].split(" ")
#         songs[song[1]] = ''.join(song[2:5])
#     else :
#         test = data[i].replace(" ", "")
#         matchCnt = 0
#         matchSong = ""
#         for song in songs :
#             if test == songs[song] :
#                 matchCnt += 1
#                 matchSong = song
#             if matchCnt == 2 :
#                 answer.append("?")
#                 break

#         if matchCnt == 1 :
#             answer.append(matchSong)
#         elif matchCnt == 0:
#             answer.append("!")
# print(answer)
    
import sys
ip = sys.stdin.readline
pt = sys.stdout.write
n,m = map(int, ip().split())
li = []
for _ in range(n):
    t = list(ip().split())
    s = t[1]
    k = ' '.join(t[2:5])
    li.append([k,s])
for _ in range(m):
    q = ip().rstrip()
    ans,c = '',0
    for a,b in li:
        if q==a:
            c += 1
            ans = b
            if c>1:
                break
    if c==0:
        pt("!\n")
    elif c==2:
        pt("?\n")
    else:
        pt(f"{ans}\n")
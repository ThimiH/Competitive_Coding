n = int(input())
scores = list(map(int,input().split()))

highScore = scores[0]
lowScore = scores[0]

answer = [0,0]

for score in scores[1:]:
    if highScore < score:
        highScore = score
        answer[0] += 1
    elif lowScore > score:
        lowScore = score
        answer[1] += 1

print(answer[0],answer[1])
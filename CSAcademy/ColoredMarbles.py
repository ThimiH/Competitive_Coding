from collections import defaultdict

#wrong

for test in range(int(input())):
    n = int(input())
    colour_counts = list(map(int,input().split()))
    counts = defaultdict(lambda: 0)
    for colour_count in colour_counts:
        counts[colour_count]+=1

    marble_count = 0
    not_sure = []
    max_colour = 0

    for colour, count in counts.items():
        marble_count += count - count%colour
        if count%colour==1:
            not_sure.append(colour)
        elif count%colour>0:
            marble_count += colour
    
    for item in not_sure:
        max_colour = max(max_colour,item)
        marble_count += item
    else:
        marble_count+=1

    print(marble_count-max_colour)



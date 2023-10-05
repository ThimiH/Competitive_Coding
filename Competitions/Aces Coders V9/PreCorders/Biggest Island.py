rows = int(input())
columns = int(input())

grid = []
areas = []

for row in range(rows):
    grid.append(list(map(int,input().split())))

to_check = [[row,column] for column in range(columns) for row in range(rows)]

def find_nearby(row,column):
    goto = [-1,0,1]
    nearby = []
    for x in goto:
        for y in goto:
            if row+x<0 or column+y<0:
                continue
            else:
                if x == 0 and y == 0:
                    continue
                else:
                    nearby.append([row+x,column+y])
    return nearby    
    
while len(to_check)>0:
    row,column = to_check[0][0],to_check[0][1]
    to_check.pop(0)
    if grid[row][column]:
        areas.append(1)
        current_check_list = []
        nearby = find_nearby(row,column)
        for place in nearby:
            if place in to_check:
                current_check_list.append(place)
        while len(current_check_list)>0:
            row,column = current_check_list[0][0],current_check_list[0][1]
            current_check_list.pop(0)
            to_check.remove([row,column])
            if grid[row][column]:
                areas[-1]+=1
                nearby = find_nearby(row,column)
                for place in nearby:
                    if place in to_check and place not in current_check_list:
                        current_check_list.append(place)

print(max(areas))
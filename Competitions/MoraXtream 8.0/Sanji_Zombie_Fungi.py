n = int(input())
cell_counts = list(map(int,input().split()))
locations = list(map(int,input().split()))

m = int(input())
fun_locations = list(map(int,input().split()))
fun_radius = list(map(int,input().split()))

special_points = []

for i in range(n):
    special_points.append((locations[i],1,i))

for i in range(m):
    special_points.append((fun_locations[i]-fun_radius[i],0,i))
    special_points.append((fun_locations[i]+fun_radius[i],2,i))

special_points = sorted(special_points, key=lambda x : (x[0],x[1]))

ans = 0

counts = [0]*m

fungi = 0

fungi_dict = dict()

for item in special_points:
    if item[1]==0:
        fungi += 1
        fungi_dict[item[2]] = None
    elif item[1]==1:
        if fungi == 0:
            ans+=cell_counts[item[2]]
        elif fungi == 1:
            counts[list(fungi_dict.keys())[0]]+=cell_counts[item[2]]
    else:
        del fungi_dict[item[2]]
        fungi -= 1
    
print(ans+max(counts))
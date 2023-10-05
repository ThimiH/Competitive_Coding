n = int(input()) 
shoe_id_list = list(map(int,input().split()))
count = [0]*1001

for shoe in shoe_id_list:
    count[shoe]+=1

answer = 0
for num in count:
    answer+=num//2

print(answer)

# shoes = {}

# for shoe_id in shoe_id_list:
#     try:
#         shoes[shoe_id] += 1
#     except:
#         shoes[shoe_id] = 1

# number_of_pairs = 0

# for shoe_set in shoes.values():
#     number_of_pairs += shoe_set//2

# print(number_of_pairs)
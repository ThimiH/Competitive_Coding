n = int(input()) 
list_a = list(map(int,input().split()))
m = int(input()) 
list_b = list(map(int,input().split()))

start_val = list_a[0]-100
a_count = [0 for _ in range(200)]
b_count = [0 for _ in range(200)]

for num in list_a:
    a_count[num-start_val]+=1

for num in list_b:
    b_count[num-start_val]+=1

ans_list = [b_count[i]-a_count[i] for i in range(200)]

for ind in range(200):
    for _ in range(ans_list[ind]):
        print(ind+start_val,end=" ")

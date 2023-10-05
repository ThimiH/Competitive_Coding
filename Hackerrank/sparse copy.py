string_list_count = int(input())

string_dict = {}

for i in range(string_list_count):
    item = input()
    try:
        string_dict[item]+=1
    except:
        string_dict[item]=1

query_list_count = int(input())

for i in range(query_list_count):
    item = input()
    try:
        print(string_dict[item])
    except:
        print(0)
#string_list = input()
#query_list = input()

#string_list = ['ab','ab','abc']
#query_list = ['ab','abc','bc']

string_list_count = int(input())

string_list = []

for i in range(string_list_count):
    item = input()
    string_list.append(item)


query_list_count = int(input())

query_list = []

for i in range(query_list_count):
    item = input()
    query_list.append(item)

qno = []

for i in query_list:

    n = 0
    for j in string_list:

        if j == i:
            
            n = n+1

        
    qno.append(n)


for i in qno:
    print(i)

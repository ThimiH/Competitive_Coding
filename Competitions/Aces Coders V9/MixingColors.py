import bisect

def insert_sorted(lst, item):
    bisect.insort_left(lst, item)

n,k = tuple(map(int,input().split()))

paints = list(map(int,input().split()))
paints.sort()

answer = 0

while len(paints)>1 and paints[0]<k:
    new_colour = paints[0]+2*paints[1]
    paints = paints[2:]
    insert_sorted(paints,new_colour)
    answer += 1

if paints[0]>=k:
    print(answer)
else:
    print(-1)

# def binary_search(sequence,value):
#     #Returns the index of lowest number in distinct value sequence that is bigger than the value.
#     length = len(sequence)
#     if length == 0:
#         return None
#     elif length == 1:
#         return 0
#     else:
#         lower_bound = 0
#         upper_bound = length-1
#         while lower_bound+1<upper_bound:
#             index = (lower_bound + upper_bound)//2
#             if sequence[index]>value:
#                 upper_bound = index
#             else:
#                 lower_bound = index
#         return upper_bound

# while len(paints)>1:
#     if paints[0]>k:
#         break
#     else:
#         new_paint = paints[0]+2*paints[1]
#         paints = paints[2:]
#         index = binary_search(paints,new_paint)
#         paints = paints[:index]+[new_paint]+paints[index:]
#     answer += 1

# if paints[0]>k:
#     print(answer)
# else:
#     print(-1)

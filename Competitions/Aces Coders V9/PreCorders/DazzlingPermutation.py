n = int(input())
order = list(map(int,input().split()))

one_still = [0]*n
left_right = [1]*n

one = order.index(1)

left = order[:one]
len_left = len(left)
right = order[one+1:]
len_right = len(right)

for num in right:
    left_right[num-1] = 0

for num in range(2,n+1):
    if left_right[num-1]:
        ind = left.index[num]
        left = left[:ind]+left[ind+1:]
        len_left -= 1
        one_still[num-1]=one_still[num-2]+num+len_left-ind
    else:
        ind = right.index[num]
        right = right[:ind]+right[ind+1:]
        len_right -= 1
        one_still[num-1]=one_still[num-2]+ind

if one_still[1]!=0:
    two_still = [0]*n
    left_right = [1]*n

    two = order.index(2)

    left = order[:two]
    len_left = len(left)
    right = order[two+1:]
    len_right = len(right)

    for num in right:
        left_right[num-1] = 0

    if left_right[0]:
        ind = left.index[1]
        left = left[:ind]+left[ind+1:]
        len_left -= 1
        two_still[1]=len_left-ind
    else:
        ind = right.index[1]
        right = right[:ind]+right[ind+1:]
        len_right -= 1
        two_still[2]=ind+1    

    for num in range(3,n+1):
        if left_right[num-1]:
            ind = left.index[num]
            left = left[:ind]+left[ind+1:]
            len_left -= 1
            two_still[num-1]=two_still[num-2]+num+len_left-ind
        else:
            ind = right.index[num]
            right = right[:ind]+right[ind+1:]
            len_right -= 1
            two_still[num-1]=two_still[num-2]+ind

for ind in range(n):
    print(max(one_still[ind],two_still[ind]),end = " ")

        



# up_down = [0 for number in range(n+1)]

# status = False

# for index in range(n):
#     if order[index] == 1:
#         down = order[:index][::-1]
#         up = order[index+1:]
#         status = True
#     elif status:
#         up_down[order[index]]=1

# answer = [0]

# for number in range(2,n+1):
#     if up_down[number]:
#         index = up.index(number)
#         answer.append(index+answer[-1])
#         up.pop(index)
#     else:
#         index = down.index(number)
#         answer.append(index+number-1+answer[-1])
#         down.pop(index)

# for value in answer:
#     print(value, end=" ")





'''
n =int(input())
seq = list(map(int, input().split()))
outlst = []

if 1<=n<=200000:
    for i in range(n):
        if i == 0 :
            outlst.append(seq.index(i+1))
        else:
            outlst.append(outlst[-1]+seq.index(i+1))

        seq.remove(i+1)

fin = list(map(str, outlst))
finstr = ' '.join(fin)
print(finstr)
'''

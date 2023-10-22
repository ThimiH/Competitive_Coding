# for test in range(int(input())):
#     n = int(input())
#     if n == 21:
#         print('The competition starts tomorrow.')
#     elif n == 22:
#         print('Today is the day!')
#     else:
#         print('The IEEEXtreme 16.0 competition starts in %d days.' %(22-n))

# for _ in range(int(input())):
#     n = int(input())
#     print('The competition starts in {} day{}.'.format(22 - n, 's' if n != 21 else '' if n == 22 else ' tomorrow' if n == 21 else ' today'))

# for _ in range(int(input())):
#  c=' competition starts '
#  n=int(input())
#  print(f'The{c}tomorrow.'if n==21 else f'The IEEEXtreme 16.0{c}in {22-n} days.'if n<21 else'Today is the day!')

for _ in range(int(input())):c=' competition starts ';n=int(input());print(f'The{c}tomorrow.'if n==21 else f'The IEEEXtreme 16.0{c}in {22-n} days.'if n<21 else'Today is the day!')


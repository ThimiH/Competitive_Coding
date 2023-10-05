N = int(input())
main_string = input()
M = int(input())
sen_word = input()

def search(pat, txt, q):
  M = len(pat)
  N = len(txt)
  d = N
  i = 0
  j = 0
  p = 0 # hash value for pattern
  t = 0 # hash value for txt
  h = 1
  ls = []

  for i in range(M-1):
    h = (h*d) % q

  for i in range(M):
    p = (d*p + ord(pat[i])) % q
    t = (d*t + ord(txt[i])) % q

  for i in range(N-M+1):
    if p == t:
      for j in range(M):
        if txt[i+j] != pat[j]:
          break
        else:
          j += 1

      if j == M:
        ls.append(i)
      
    if i < N-M:
      t = (d*(t-ord(txt[i])*h) + ord(txt[i+M])) % q

      if t < 0:
        t = t+q

  return ls

import random

def choose_q():
    # Generate a random prime number in a suitable range
    while True:
        q = random.randint(10000, 100000)  # Adjust the range as needed
        if is_prime(q):
            return q
        
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

txt = main_string
pat = sen_word

q = choose_q
ans = search(pat, txt, q)

if len(ans)>0:
    ans2=[ans[0],ans[0]+M]
    clash = False
    for value in ans[1:]:
        if ans2[-1]<value:
            ans2.append(value)
            ans2.append(value+M)
        else:
            ans2[-1]=value+M

    print(txt[0:ans2[0]],end="")
    for i,index in enumerate(ans2[:-1]):
        print("#",end="")
        print(txt[index:ans2[i+1]],end="")

    print("#",end="")
    print(txt[ans2[-1]:])
else:
    print(txt)

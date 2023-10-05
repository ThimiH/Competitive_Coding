text = str(input())
pat = str(input())

count = 0

length_pat = len(pat)
length_text = len(text)

for index in range(length_pat,length_text+1):
    if pat == text[index-length_pat:index]:
        count += 1

print(count)
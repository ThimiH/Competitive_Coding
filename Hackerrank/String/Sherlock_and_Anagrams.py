for test in range(int(input())):
    s = input()
    n = len(s)
    count = 0
    for l in range(1, n):
        d = {}
        for i in range(n - l + 1):
            subs = ''.join(sorted(s[i:i + l]))
            if subs in d:
                count += d[subs]
                d[subs] += 1
            else:
                d[subs] = 1
    print(count)
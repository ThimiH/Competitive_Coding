for test in range(int(input())):
    data = list(map(int,input().split()))
    if data[0] == 0:
        print(1)
    else:
        data = data[1:]
        dset = set()
        for angle in data:
            if angle<0:
                dset.add((angle%180+360)%180)
            else:
                dset.add(angle%180)
        print(len(dset)*2)
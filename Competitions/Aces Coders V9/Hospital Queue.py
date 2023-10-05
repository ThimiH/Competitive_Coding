t = int(input())

for Testcase in range(t):
    p, n = tuple(map(int,input().split()))
    times = list(map(int,input().split()))

    patients_per_minute = 0

    for time in times:
        patients_per_minute += 1/time

    #print(patients_per_minute)
    
    test_time = max(int(p//patients_per_minute)-max(times),0)

    test_time_list = []

    patients_done = 0

    for index in range(n):
        if test_time > times[index]:
            test_time_list.append(-1*(test_time%times[index]))
        else: 
            test_time_list.append(times[index]-test_time)
        patients_done += test_time//times[index]

    #print(test_time,patients_done)
        
    while patients_done<=p:
        index = test_time_list.index(min(test_time_list))
        #print(index, end=' ')
        #print(test_time_list[index], end=' ')
        #print(patients_done, end=' ')
        test_time_list[index] += times[index]
        patients_done+=1

    #print()
    print(index+1)



'''
t = int(input())

for Testcase in range(t):
    p, n = tuple(map(int,input().split()))
    times = list(map(int,input().split()))
    timesnow = times[:]
    if p > n:
        p -= n
        while True:
            mintime = min(timesnow)
            count = 0
            for ind in range(n):
                if timesnow[ind] == mintime:
                    timesnow[ind] = times[ind]
                    count+=1
                    if count == p+1:
                        state = 1
                        print(ind+1)
                else:
                    timesnow[ind]-= mintime
            p -= count
            if state == 1:
                break
    else:
        print(p)
'''
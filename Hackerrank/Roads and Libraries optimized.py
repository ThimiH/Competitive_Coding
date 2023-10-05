def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib<=c_road:
        return n*c_lib
    
    else:
        roaddict = {}
        for road in cities:
            try:
                roaddict[road[0]].append(road[1])
            except:
                roaddict[road[0]] = [road[1]]
            try:
                roaddict[road[1]].append(road[0])
            except:
                roaddict[road[1]] = [road[0]]
        
        city = list(range(1,n+1))
        cityq = []
        trees = 0

        while len(city)>0:
            try:
                for town in roaddict[city[0]]:
                    if town in city:
                        cityq.append(town)
                        city.remove(town)
                city.remove(city[0])
            except:
                city.remove(city[0])
            
            while len(cityq)>0:
                try:
                    for town in roaddict[cityq[0]]:
                        if town in city:
                            cityq.append(town)
                            city.remove(town)
                    cityq.remove(cityq[0])
                except:
                    cityq.remove(cityq[0])
            trees+=1

        return trees*c_lib+(n-trees)*c_road

print(roadsAndLibraries(5, 6, 1, [[1,2],[1,3],[1,4]]))
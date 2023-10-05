def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib<=c_road:
        return n*c_lib
    
    else:
        city = list(range(1,n+1))
        cityq = []
        trees = 0
        while len(city)>0:
            for road in cities.copy():
                if road[0]==city[0]:
                    if road[1] in city:
                        cityq.append(road[1])
                        city.remove(road[1])
                        cities.remove(road)
                        
                if road[1]==city[0]:
                    if road[0] in city:
                        cityq.append(road[0])
                        city.remove(road[0])
                        cities.remove(road)
            city.remove(city[0])

            while len(cityq)>0:

                for road in cities.copy():
                    if road[0]==cityq[0]:
                        if road[1] in city:
                            cityq.append(road[1])
                            city.remove(road[1])
                            cities.remove(road)
                            
                    if road[1]==cityq[0]:
                        if road[0] in city:
                            cityq.append(road[0])
                            city.remove(road[0])
                            cities.remove(road)
                cityq.remove(cityq[0])

            trees+=1
        return trees*c_lib+(n-trees)*c_road

print(roadsAndLibraries(5, 6, 1, [[1,2],[1,3],[1,4]]))
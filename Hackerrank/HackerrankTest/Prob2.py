def check(grid,n,m):
    for y in range(n):
        for x in range(m):
            if 1<=grid[y][x]<=100:
                continue
            else:
                return False
    return True

def numCells(grid):
    # Write your code here
    n = len(grid)
    m = len(grid[0])
    ans = 0
    if 1<=n<=500 and 1<=m<=500 and check(grid,n,m):
        for y in range(1,n):
            for x in range(1,m):
                n1,n2,n3,n4,n5,n6,n7,n8 = (0,0,0,0,0,0,0,0)
                n0 = grid[y][x]
                try:
                    n1 = grid[y-1][x-1]
                except:
                    pass
                
                try:
                    n2 = grid[y-1][x]
                except:
                    pass
                
                try:
                    n3 = grid[y-1][x+1]
                except:
                    pass
                
                try:
                    n4 = grid[y][x+1]
                except:
                    pass
                
                try:
                    n5 = grid[y+1][x+1]
                except:
                    pass
                
                try:
                    n6 = grid[y+1][x]
                except:
                    pass
                
                try:
                    n7 = grid[y+1][x-1]
                except:
                    pass
                
                try:
                    n8 = grid[y][x-1]
                except:
                    pass

                if n0>n1 and n0>n2 and n0>n3 and n0>n4 and n0>n5 and n0>n6 and n0>n7 and n0>n8:
                    ans += 1

        for y in range(0,1):
            for x in range(1,m):
                n1,n2,n3,n4,n5,n6,n7,n8 = (0,0,0,0,0,0,0,0)
                n0 = grid[y][x]
                try:
                    n4 = grid[y][x+1]
                except:
                    pass
                
                try:
                    n5 = grid[y+1][x+1]
                except:
                    pass
                
                try:
                    n6 = grid[y+1][x]
                except:
                    pass
                
                try:
                    n7 = grid[y+1][x-1]
                except:
                    pass
                
                try:
                    n8 = grid[y][x-1]
                except:
                    pass

                if n0>n1 and n0>n2 and n0>n3 and n0>n4 and n0>n5 and n0>n6 and n0>n7 and n0>n8:
                    ans += 1

        for y in range(1,n):
            for x in range(0,1):
                n1,n2,n3,n4,n5,n6,n7,n8 = (0,0,0,0,0,0,0,0)
                n0 = grid[y][x]
                
                
                try:
                    n2 = grid[y-1][x]
                except:
                    pass
                
                try:
                    n3 = grid[y-1][x+1]
                except:
                    pass
                
                try:
                    n4 = grid[y][x+1]
                except:
                    pass
                
                try:
                    n5 = grid[y+1][x+1]
                except:
                    pass
                
                try:
                    n6 = grid[y+1][x]
                except:
                    pass

                if n0>n1 and n0>n2 and n0>n3 and n0>n4 and n0>n5 and n0>n6 and n0>n7 and n0>n8:
                    ans += 1

        for y in range(0,1):
            for x in range(0,1):
                n1,n2,n3,n4,n5,n6,n7,n8 = (0,0,0,0,0,0,0,0)
                n0 = grid[y][x]
                
                
                
                try:
                    n4 = grid[y][x+1]
                except:
                    pass
                
                try:
                    n5 = grid[y+1][x+1]
                except:
                    pass
                
                try:
                    n6 = grid[y+1][x]
                except:
                    pass

                if n0>n1 and n0>n2 and n0>n3 and n0>n4 and n0>n5 and n0>n6 and n0>n7 and n0>n8:
                    ans += 1
    
    return ans
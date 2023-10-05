def matrix_multiply(arr1,arr2):
    MOD = 10**9+7
    a = (arr1[0][0]*arr2[0][0]+arr1[0][1]*arr2[1][0])%MOD
    b = (arr1[0][0]*arr2[0][1]+arr1[0][1]*arr2[1][1])%MOD
    c = (arr1[1][0]*arr2[0][0]+arr1[1][1]*arr2[1][0])%MOD
    d = (arr1[1][0]*arr2[0][1]+arr1[1][1]*arr2[1][1])%MOD
    return [[a,b],[c,d]]

powers_of_two = [[[1,1],[1,0]]]

n = bin(int(input()))[2:][::-1]

for i in range(1,len(n)):
    powers_of_two.append(matrix_multiply(powers_of_two[-1],powers_of_two[-1]))

ans = [[1,0],[0,1]]

for ind in range(len(n)):
    if int(n[ind]):
        ans = matrix_multiply(ans,powers_of_two[ind])

print(ans[0][1])
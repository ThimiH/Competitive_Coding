n = int(input());
# dp = [[0 for i in range(n)] for j in range(n)];

a = input()[1:-1]
x,y = tuple(map(int,a.split(",")));
b = input()[1:-1]
tx,ty = tuple(map(int,b.split(",")));

dx = abs(x-tx)
dy = abs(y-ty)
k = round(max(dx/2,dy/2,(dx+dy)/3))
ans = k+(k+dx+dy)%2

if n>x and n>y and n>tx and n>ty:
  print(ans-1)
else:
  print(-1)



# def getsteps(x, y, tx, ty):
#   if (x == tx and y == ty):
#     return dp[0][0];

#   elif(dp[abs(x - tx)][abs(y - ty)] != 0):
#     return dp[abs(x - tx)][abs(y - ty)];
#   else:

#     x1, y1, x2, y2 = 0, 0, 0, 0;

#     if (x <= tx):
#       if (y <= ty):
#         x1 = x + 2;
#         y1 = y + 1;
#         x2 = x + 1;
#         y2 = y + 2;
#       else:
#         x1 = x + 2;
#         y1 = y - 1;
#         x2 = x + 1;
#         y2 = y - 2;

#     elif (y <= ty):
#       x1 = x - 2;
#       y1 = y + 1;
#       x2 = x - 1;
#       y2 = y + 2;
#     else:
#       x1 = x - 2;
#       y1 = y - 1;
#       x2 = x - 1;
#       y2 = y - 2;

#     dp[abs(x - tx)][abs(y - ty)] = \
#     min(getsteps(x1, y1, tx, ty),
#     getsteps(x2, y2, tx, ty)) + 1;

#     dp[abs(y - ty)][abs(x - tx)] = \
#     dp[abs(x - tx)][abs(y - ty)];
#     return dp[abs(x - tx)][abs(y - ty)];

# if ((x == 1 and y == 1 and tx == 2 and ty == 2) or
#     (x == 2 and y == 2 and tx == 1 and ty == 1)):
#   ans = 4;
# elif ((x == 1 and y == n and tx == 2 and ty == n - 1) or
#   (x == 2 and y == n - 1 and tx == 1 and ty == n)):
#   ans = 4;
# elif ((x == n and y == 1 and tx == n - 1 and ty == 2) or
#   (x == n - 1 and y == 2 and tx == n and ty == 1)):
#   ans = 4;
# elif ((x == n and y == n and tx == n - 1 and ty == n - 1)
#   or (x == n - 1 and y == n - 1 and tx == n and ty == n)):
#   ans = 4;
# else:

#   dp[1][0] = 3;
#   dp[0][1] = 3;
#   dp[1][1] = 2;
#   dp[2][0] = 2;
#   dp[0][2] = 2;
#   dp[2][1] = 1;
#   dp[1][2] = 1;

#   ans = getsteps(x, y, tx, ty);

# print(ans-1);

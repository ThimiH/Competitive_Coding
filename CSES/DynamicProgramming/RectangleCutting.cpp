#include <iostream>
#include <vector>
#include <limits>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    vector<vector<int>> dp(b, vector<int>(a, numeric_limits<int>::max()));

    for (int i = 0; i < a; i++) {
        dp[0][i] = i;
    }

    for (int i = 0; i < b; i++) {
        dp[i][0] = i;
    }

    for (int j = 1; j < b; j++) {
        for (int i = 1; i < a; i++) {
            if (i == j) {
                dp[j][i] = 0;
            } else {
                for (int n = 1; n <= a / 2; n++) {
                    if (i - n - 1 >= 0) {
                        dp[j][i] = min(dp[j][i], dp[j][n] + dp[j][i - n - 1] + 1);
                    }
                }
                for (int m = 1; m <= b / 2; m++) {
                    if (j - m - 1 >= 0) {
                        dp[j][i] = min(dp[j][i], dp[m][i] + dp[j - m - 1][i] + 1);
                    }
                }
            }
        }
    }

    cout << dp[b - 1][a - 1] << endl;

    return 0;
}
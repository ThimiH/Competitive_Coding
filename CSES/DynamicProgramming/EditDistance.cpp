#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    string a, b;
    cin >> a;
    int n = a.length();
    cin >> b;
    int m = b.length();

    vector<vector<int>> dp(m, vector<int>(n, 0));

    if (a[0] == b[0]) {
        dp[0][0] = 0;
    } else {
        dp[0][0] = 1;
    }

    for (int i = 1; i < n; i++) {
        dp[0][i] = dp[0][i - 1] + 1;
    }

    for (int i = 1; i < m; i++) {
        dp[i][0] = dp[i - 1][0] + 1;
    }

    for (int j = 1; j < m; j++) {
        for (int i = 1; i < n; i++) {
            if (a[i] == b[j]) {
                dp[j][i] = dp[j - 1][i - 1];
            } else {
                dp[j][i] = min(min(dp[j - 1][i], dp[j][i - 1]), dp[j - 1][i - 1]) + 1;
            }
        }
    }

    cout << dp[m - 1][n - 1] << endl;

    return 0;
}

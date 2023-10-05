#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, x;
    cin >> n >> x;

    vector<int> prices(n);
    vector<int> pages(n);

    for (int i = 0; i < n; i++) {
        cin >> prices[i];
    }

    for (int i = 0; i < n; i++) {
        cin >> pages[i];
    }

    vector<pair<int, int>> zipped_data;
    for (int i = 0; i < n; i++) {
        zipped_data.push_back(make_pair(prices[i], pages[i]));
    }

    sort(zipped_data.begin(), zipped_data.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
        return a.first < b.first;
    });

    for (int i = 0; i < n; i++) {
        prices[i] = zipped_data[i].first;
        pages[i] = zipped_data[i].second;
    }

    vector<vector<int>> dp(2, vector<int>(x + 1, 0));

    for (int j = 1; j <= n; j++) {
        for (int i = 1; i <= x; i++) {
            if (i < prices[j - 1]) {
                continue;
            } else {
                dp[1][i] = max(dp[0][i], dp[0][i - prices[j - 1]] + pages[j - 1]);
            }
        }
        dp[0] = dp[1];
    }

    cout << dp[0][x] << endl;

    return 0;
}

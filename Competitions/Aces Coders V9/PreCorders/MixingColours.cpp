#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void insertSorted(vector<int>& lst, int item) {
    lst.insert(lower_bound(lst.begin(), lst.end(), item), item);
}

int main() {
    int n, k;
    cin >> n >> k;
    
    vector<int> paints(n);
    for (int i = 0; i < n; i++) {
        cin >> paints[i];
    }
    
    sort(paints.begin(), paints.end());
    
    int answer = 0;
    
    while (paints.size() > 1 && paints[0] < k) {
        int new_colour = paints[0] + 2 * paints[1];
        paints.erase(paints.begin(), paints.begin() + 2);
        insertSorted(paints, new_colour);
        answer++;
    }
    
    if (paints[0] >= k) {
        cout << answer << endl;
    } else {
        cout << -1 << endl;
    }
    
    return 0;
}
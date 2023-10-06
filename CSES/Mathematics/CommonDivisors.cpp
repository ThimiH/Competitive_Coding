#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> numbers(n);

    for (int i = 0; i < n; ++i) {
        cin >> numbers[i];
    }

    sort(numbers.rbegin(), numbers.rend());

    for (int divisor = numbers[0]; divisor >= 1; --divisor) {
        int count = 0;
        for (int number : numbers) {
            if (number < divisor) {
                break;
            }
            if (number % divisor == 0) {
                count += 1;
            }
        }
        if (count > 1) {
            cout << divisor << endl;
            break;
        }
    }

    return 0;
}

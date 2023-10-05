#include <iostream>
#include <vector>
#include <unordered_map>

std::vector<int> SOE(int n) {
    std::vector<int> primes;
    std::vector<bool> val(n + 1, true);
    val[0] = val[1] = false;
    
    for (int ind = 2; ind * ind <= n; ++ind) {
        if (val[ind]) {
            for (int x = ind * ind; x <= n; x += ind) {
                val[x] = false;
            }
        }
    }

    for (int y = 0; y <= n; ++y) {
        if (val[y]) {
            primes.push_back(y);
        }
    }

    return primes;
}

int main() {
    std::vector<int> primes = SOE(5 * 100000);

    int testCases;
    std::cin >> testCases;

    while (testCases--) {
        int x;
        std::cin >> x;
        int i = 0;
        std::unordered_map<int, int> prime_factors;

        while (i < primes.size() && primes[i] <= x) {
            if (x % primes[i] == 0) {
                x = x / primes[i];
                if (prime_factors.find(primes[i]) != prime_factors.end()) {
                    prime_factors[primes[i]] += 1;
                } else {
                    prime_factors[primes[i]] = 1;
                }
            } else {
                i += 1;
            }
        }

        int ans = 1;
        for (const auto& kv : prime_factors) {
            ans *= (kv.second + 1);
        }

        if (ans == 1) {
            ans = 2;
        }

        std::cout << ans << std::endl;
    }

    return 0;
}

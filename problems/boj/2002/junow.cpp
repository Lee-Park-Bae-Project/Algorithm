#include <bits/stdc++.h>

using namespace std;

int n, ans;
map<string, int> a, b;
vector<int> v;

int main(void) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cin >> n;

  string t;
  for (int i = 0; i < n; i++) {
    cin >> t;
    a[t] = i;
  }
  v.resize(n);
  for (int i = 0; i < n; i++) {
    cin >> t;
    v[i] = a[t];
  }

  for (int i = 0; i < n - 1; i++) {
    for (int j = i + 1; j < n; j++) {
      if (v[i] > v[j]) {
        ans++;
        break;
      }
    }
  }
  cout << ans << "\n";

  return 0;
}

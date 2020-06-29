#include <bits/stdc++.h>

using namespace std;
int n, m;
vector<string> a, ans;
int main(void) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cin >> n >> m;
  string t;
  a.resize(n);

  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }
  sort(a.begin(), a.end());

  for (int j = 0; j < m; j++) {
    cin >> t;
    if (binary_search(a.begin(), a.end(), t)) {
      ans.push_back(t);
    }
  }

  sort(ans.begin(), ans.end());

  cout << ans.size() << "\n";
  for (auto _s : ans) {
    cout << _s << "\n";
  }

  return 0;
}
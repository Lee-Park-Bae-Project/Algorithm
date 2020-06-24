#include <bits/stdc++.h>

using namespace std;
int n, k, ans;
vector<string> check;
bool selected[26];

vector<int> bm;

int main(void) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> n >> k;
  if (k == 26) {
    cout << n << "\n";
    return 0;
  }
  if (k < 5) {
    cout << 0;
    return 0;
  }
  string s;
  bm.resize(n);

  for (int i = 0; i < n; i++) {
    cin >> s;
    int len = s.size();
    for (int j = 0; j < len; j++) {
      bm[i] |= (1 << (s[j] - 'a'));
    }
  }

  cout << ans << "\n";

  return 0;
}
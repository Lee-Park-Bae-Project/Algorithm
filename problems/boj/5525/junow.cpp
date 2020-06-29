#include <bits/stdc++.h>

using namespace std;

int n, m, ans, cnt;
string s;

int main(void) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cin >> n >> m >> s;

  for (int i = 0; i < m - 1; i++) {
    if (s[i] == 'O' && s[i + 1] == 'I') {
      if (cnt == n) {
        ans++;
        cnt--;
      }

    } else if (s[i] == 'I' && s[i + 1] == 'O') {
      cnt++;
    } else {
      cnt = 0;
    }
  }

  cout << ans << "\n";

  return 0;
}
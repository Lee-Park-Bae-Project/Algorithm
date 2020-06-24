#include <bits/stdc++.h>

using namespace std;

int n, idx;
string s[100];
int main(void) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> s[i];
  }
  idx = -1;
  for (int i = 0; i < n; i++) {
    for (int j = i; j < n; j++) {
      if (s[i].size() != s[j].size()) continue;
      int len = s[i].size();
      bool flag = true;
      for (int k = 0; k < len; k++) {
        if (s[i][k] != s[j][len - 1 - k]) {
          flag = false;
          break;
        }
      }
      if (flag) {
        idx = i;
        break;
      }
    }
    if (idx >= 0) {
      break;
    }
  }

  cout << s[idx].size() << " " << s[idx][s[idx].size() / 2];

  return 0;
}
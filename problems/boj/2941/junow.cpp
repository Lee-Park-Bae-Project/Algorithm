#include <bits/stdc++.h>

using namespace std;

int i, ans;
string s, ss[8] = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};

int main(void) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cin >> s;
  int len = s.size();

  while (i < len) {
    int idx = -1, j = 0;
    for (; j < 8; j++) {
      idx = s.find(ss[j], i);
      if (idx < 0 || idx != i) continue;

      ans++;
      i = idx + ss[j].size();
      break;
    }
    if (j == 8) {
      ans++;
      i++;
    }
  }

  cout << ans << "\n";

  return 0;
}
#include <bits/stdc++.h>

using namespace std;
int n, k, ans;
vector<string> check;
bool selected[26];

void dfs(int _i, int cnt) {
  if (cnt == k - 5) {
    int candi = 0;
    for (int i = 0; i < n; i++) {
      bool flag = true;
      for (int j = 0; j < check[i].size(); j++) {
        if (!selected[check[i][j] - 'a']) {
          flag = false;
          break;
        }
      }
      if (flag) {
        candi++;
      }
    }

    ans = max(ans, candi);
    return;
  }

  for (int i = _i; i < 26; i++) {
    if (selected[i]) continue;
    selected[i] = 1;
    dfs(i, cnt + 1);
    selected[i] = 0;
  }
}

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

  for (int i = 0; i < n; i++) {
    cin >> s;
    int len = s.size();
    string t = "";
    for (int j = 4; j < len - 4; j++) {
      t += s[j];
    }
    check.push_back(t);
  }

  selected[0] = true;
  selected[2] = true;
  selected[8] = true;
  selected[13] = true;
  selected[19] = true;

  dfs(0, 0);

  cout << ans << "\n";

  return 0;
}
#include <bits/stdc++.h>

using namespace std;

int n, m;
int a[50], b[10000];

bool cmp(const int& a, const int& b) {
  return a > b;
}
int main(void) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> n;
  for (int i = 0; i < n; i++) cin >> a[i];
  cin >> m;
  for (int i = 0; i < m; i++) cin >> b[i];

  sort(a, a + n, cmp);
  sort(b, b + m, cmp);

  int i = 0, j = 0;
  int ans = 0;
  if (a[0] < b[0]) {
    cout << "-1\n";
    return 0;
  }

  int cnt = 0;
  while (1) {
    if (cnt >= m) {
      break;
    }
    int i = 0;
    int j = 0;
    while (i < n && j < m) {
      if (a[i] >= b[j]) {
        i++;
        j++;
        cnt++;
      } else {
        j++;
      }

      if (cnt == m) {
        break;
      }

      if (i == n) {
        i = 0;
        j = 0;
        ans++;
      }
    }

    ans++;
  }

  cout << ans << "\n";
  return 0;
}
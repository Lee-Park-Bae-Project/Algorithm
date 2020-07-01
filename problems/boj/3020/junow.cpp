#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

int N, H;
vi a, b;

int main(void) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cin >> N >> H;
  a.resize(N / 2);
  b.resize(N / 2);
  for (int i = 0; i < N; i++) {
    if (i % 2 == 0) {
      cin >> a[i];
    } else {
      cin >> b[i];
    }
  }

  sort(a.begin(), a.end());
  sort(b.begin(), b.end());

  int l = 1, r = H;
  int ans = INT_MAX, cnt = 0;
  while (l <= r) {
    int m = (l + r) / 2;
    int hit1 = lower_bound(a.begin(), a.end(), m) - a.begin();      // bottom
    int hit2 = lower_bound(b.begin(), b.end(), H - m) - b.begin();  // top

    if (ans == hit1 + hit2) {
      cnt++;
    } else if (ans > hit1 + hit2) {
      cnt = 1;
      ans = hit1 + hit2;
    }

    if (hit1 <= hit2) {
      r = m - 1;
    } else {
      l = m + 1;
    }
  }

  cout << ans << " " << cnt << "\n";
  return 0;
}

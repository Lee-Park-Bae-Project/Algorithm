#include <bits/stdc++.h>

using namespace std;

const int MAX = 300000;
int n, k, c[MAX];
pair<int, int> a[MAX];
priority_queue<int> pq;

long long ans;

int main(void) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> n >> k;
  int t1, t2;
  for (int i = 0; i < n; i++) {
    cin >> t1 >> t2;
    a[i] = {t1, t2};
  }

  for (int i = 0; i < k; i++) {
    cin >> c[i];
  }

  sort(c, c + k);
  sort(a, a + n);

  int ji = 0;

  for (int i = 0; i < k; i++) {
    while (ji < n && a[ji].first <= c[i]) {
      pq.push(a[ji].second);
      ji++;
    }

    if (!pq.empty()) {
      int maxValue = pq.top();
      pq.pop();
      ans += maxValue;
    }
  }

  cout << ans << "\n";

  return 0;
}
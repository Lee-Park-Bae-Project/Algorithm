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
    // 제일 무거운 화물이 제일 쎈 크레인보다 무거우면 못 옮김
    cout << "-1\n";
    return 0;
  }

  int cnt = 0;
  while (1) {
    if (cnt >= m) {
      // 전체 다 옮겼으면 그만둠
      break;
    }
    int i = 0;
    int j = 0;

    while (i < n && j < m) {
      if (a[i] >= b[j]) {
        // i 번째 크레인이 j 번쨰 화물 옮길 수 있는 경우
        i++;  // 다음 크레인
        j++;  // 다음 화물
        cnt++;
      } else {
        // 못 옮기면 다음 화물 확인
        j++;
      }
    }
    ans++;
  }

  cout << ans << "\n";
  return 0;
}
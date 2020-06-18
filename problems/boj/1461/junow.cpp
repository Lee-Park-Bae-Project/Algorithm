#include <bits/stdc++.h>

using namespace std;

int N, M, ans;
int arr[10000];

bool cmp(const int& a, const int& b) {
  return a > b;
}

int main(void) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  vector<int> v1, v2;
  int mm = 0;

  cin >> N >> M;
  for (int i = 0; i < N; i++) {
    cin >> arr[i];
    mm = max(mm, abs(arr[i]));
    if (arr[i] < 0)
      v1.push_back(arr[i]);
    else
      v2.push_back(arr[i]);
  }

  sort(v1.begin(), v1.end());
  sort(v2.begin(), v2.end(), cmp);

  for (int i = 0, len = v1.size(); i < len; i += M) {
    ans += abs(v1[i] * 2);
  }

  for (int i = 0, len = v2.size(); i < len; i += M) {
    ans += abs(v2[i] * 2);
  }

  cout << ans - mm << "\n";
  return 0;
}

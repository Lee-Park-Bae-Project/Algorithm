#include <bits/stdc++.h>

using namespace std;
int N;
int arr[500000];

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> N;

  for (int i = 0; i < N; i++) {
    cin >> arr[i];
  }

  sort(arr, arr + N);

  long long ans = 0;
  for (int i = 0; i < N; i++) {
    ans += abs(arr[i] - (i + 1));
  }
  cout << ans << "\n";
  return 0;
}

#include <bits/stdc++.h>

using namespace std;
int N, L, ans;
int arr[1001];
int main(void)
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> N >> L;
  for (int i = 0; i < N; i++)
  {
    cin >> arr[i];
  }
  sort(arr, arr + N);

  ans = 0;
  int i = 0;
  int s = 0;
  while (i < N)
  {
    s = i;
    while (arr[i] - arr[s] < L)
    {
      i++;
    }
    ans++;
  }

  cout << ans << '\n';
  return 0;
}
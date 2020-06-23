#include <bits/stdc++.h>

using namespace std;

int N, M;
int pack[50];
int one[50];

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  int min1 = 1001, min2 = 1001;

  cin >> N >> M;
  for (int i = 0; i < M; i++) {
    cin >> pack[i] >> one[i];
    min1 = min(min1, pack[i]);
    min2 = min(min2, one[i]);
  }

  cout << min(((N / 6) + 1) * min1, min((N / 6) * min1 + (N % 6) * min2, N * min2));

  return 0;
}
#include <bits/stdc++.h>

using namespace std;

int N, M;
string s;

char board1[51][51];
char board2[51][51];

bool check() {
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      if (board1[i][j] != board2[i][j]) {
        return false;
      }
    }
  }
  return true;
}

void flip(int r, int c) {
  for (int i = r; i < r + 3; i++) {
    for (int j = c; j < c + 3; j++) {
      board1[i][j] = '0' ^ '1' ^ board1[i][j];
    }
  }
}

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cin >> N >> M;
  int ans = 0;

  for (int i = 0; i < N; i++) {
    cin >> board1[i];
  }

  for (int i = 0; i < N; i++) {
    cin >> board2[i];
  }

  for (int i = 0; i < N - 2; i++) {
    for (int j = 0; j < M - 2; j++) {
      if (board1[i][j] != board2[i][j]) {
        flip(i, j);
        ans++;
      }
    }
  }

  if (check()) {
    cout << ans << "\n";
  } else {
    cout << -1 << "\n";
  }
  return 0;
}
#include <iostream>

using namespace std;

const int dy[3] = {-1, 0, 1};
const int dx[3] = {1, 1, 1};

int r, c, ans;
char board[10000][500];
char ch;

bool bfs(int y, int x) {
  if (x == c - 1) return true;
  for (int dir = 0; dir < 3; dir++) {
    int ny = y + dy[dir];
    int nx = x + dx[dir];

    if (ny >= r || ny < 0 || nx >= c || nx < 0) continue;
    if (board[ny][nx] == 'x') continue;

    board[ny][nx] = 'x';
    if (bfs(ny, nx)) return true;
  }
  return false;
}
int main(void) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> r >> c;

  for (int i = 0; i < r; i++) {
    cin >> board[i];
  }

  for (int i = 0; i < r; i++) {
    if (bfs(i, 0)) ans++;
  }

  cout << ans << "\n";

  return 0;
}

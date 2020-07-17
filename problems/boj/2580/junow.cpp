#include <bits/stdc++.h>
#define endl "\n"

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<pair<int, int>> vpii;

const int dy[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
const int dx[8] = {-1, 0, 1, -1, 1, -1, 0, 1};

int cnt, board[9][9];
vi holes;

int toNum(int i, int j) {
  return i * 9 + j;
}
pii toPos(int num) {
  return {num / 9, num % 9};
}

pii getCenter(int y, int x) {
  return {(y / 3) * 3 + 1, (x / 3) * 3 + 1};
}
bool checkLine(int y, int x, int n) {
  for (int i = 0; i < 9; i++) {
    if (board[y][i] == n || board[i][x] == n) return false;
  }
  return true;
}

bool checkRec(int y, int x, int n) {
  pii center = getCenter(y, x);
  int center_y = center.first;
  int center_x = center.second;
  for (int dir = 0; dir < 8; dir++) {
    int ny = center_y + dy[dir];
    int nx = center_x + dx[dir];
    if (board[ny][nx] == n) return false;
  }
  if (board[center_y][center_x] == n) return false;
  return true;
}

int getHole() {
  for (int i = 0; i < 9; i++) {
    for (int j = 0; j < 9; j++) {
      if (board[i][j] == 0) return toNum(i, j);
    }
  }
  return -1;
}
void dfs() {
  int hole = getHole();
  if (hole == -1) {
    for (int i = 0; i < 9; i++) {
      for (int j = 0; j < 9; j++) {
        cout << board[i][j] << " ";
      }
      cout << endl;
    }
    exit(0);
  }
  pii cur = toPos(hole);
  int y = cur.first;
  int x = cur.second;
  for (int k = 1; k <= 9; k++) {
    if (checkLine(y, x, k) && checkRec(y, x, k)) {
      board[y][x] = k;
      dfs();
      board[y][x] = 0;
    }
  }
}

int main(void) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  for (int i = 0; i < 9; i++) {
    for (int j = 0; j < 9; j++) {
      cin >> board[i][j];
    }
  }

  dfs();

  return 0;
}

#include <bits/stdc++.h>
#define endl "\n"

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<pair<int, int>> vpii;
typedef vector<vector<int>> vvi;

const int dy[4] = {-1, 0, 1, 0};
const int dx[4] = {0, 1, 0, -1};

struct INFO {
  pii prev;
  pii cur;
  int v;
};
int n, ans = INT_MAX;
const int CORNER_PRICE = 500;
const int LINE_PRICE = 100;
vvi board;

bool isCorner(pii prev, pii next) {
  return abs(prev.first - next.first) == 1 && abs(prev.second - next.second) == 1;
}

void bfs() {
  int n = board.size();
  queue<INFO> q;
  q.push({{0, 0}, {0, 0}, 0});

  while (!q.empty()) {
    auto cur = q.front();
    q.pop();
    if (cur.cur.first == n - 1 && cur.cur.second == n - 1) {
      ans = min(ans, cur.v);
      continue;
    }
    for (int dir = 0; dir < 4; dir++) {
      int ny = cur.cur.first + dy[dir];
      int nx = cur.cur.second + dx[dir];
      int nextV = cur.v + LINE_PRICE;
      if (isCorner(cur.prev, {ny, nx})) nextV += CORNER_PRICE;
      if (ny < 0 || nx < 0 || ny >= n || nx >= n) continue;
      if (board[ny][nx] == 0 || board[ny][nx] >= nextV) {
        board[ny][nx] = nextV;
        q.push({{cur.cur}, {ny, nx}, nextV});
      }
    }
  }
}

int solution(vector<vector<int>> _board) {
  int answer = 0;
  board = _board;

  bfs();
  return ans;
}

int main(void) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  vvi board0 = {{0, 0}, {1, 0}};
  vvi board1 = {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}};
  vvi board2 = {{0, 0, 0, 0, 0, 0, 0, 1},
                {0, 0, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 1, 0, 0},
                {0, 0, 0, 0, 1, 0, 0, 0},
                {0, 0, 0, 1, 0, 0, 0, 1},
                {0, 0, 1, 0, 0, 0, 1, 0},
                {0, 1, 0, 0, 0, 1, 0, 0},
                {1, 0, 0, 0, 0, 0, 0, 0}};
  vvi board3 = {{0, 0, 1, 0},
                {0, 0, 0, 0},
                {0, 1, 0, 1},
                {1, 0, 0, 0}};
  vvi board4 = {{0, 0, 0, 0, 0, 0},
                {0, 1, 1, 1, 1, 0},
                {0, 0, 1, 0, 0, 0},
                {1, 0, 0, 1, 0, 1},
                {0, 1, 0, 0, 0, 1},
                {0, 0, 0, 0, 0, 0}};

  cout << solution(board3) << endl;

  return 0;
}
#include <bits/stdc++.h>
#define endl "\n"

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<pair<int, int>> vpii;

const int dy[4] = {-1, 0, 1, 0};
const int dx[4] = {0, 1, 0, -1};

int n, m, selected[9];
bool visit[9];
void dfs(int cnt, int idx) {
  if (cnt == m) {
    for (int i = 0; i < m; i++) {
      cout << selected[i] << " ";
    }
    cout << endl;
    return;
  }

  for (int i = idx; i < n; i++) {
    if (visit[i]) continue;
    visit[i] = true;
    selected[cnt] = i + 1;
    dfs(cnt + 1, i + 1);
    visit[i] = false;
  }
}

int main(void) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> n >> m;

  dfs(0, 0);
  return 0;
}

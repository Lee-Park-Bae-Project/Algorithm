#include <bits/stdc++.h>
#define endl "\n"

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<pair<int, int>> vpii;

const int dy[4] = {-1, 0, 1, 0};
const int dx[4] = {0, 1, 0, -1};

const int MAX = 10000000;
int tc, ans;
bool che[MAX];

string s;

bool selected[7];

void makeChe() {
  fill(&che[0], &che[MAX], true);
  che[0] = che[1] = false;
  for (int i = 2; i <= MAX; i++) {
    if (!che[i]) continue;
    for (int j = i + i; j <= MAX; j += i) {
      che[j] = false;
    }
  }
}

void bt(int maxLen, string& s, string& cur, set<int>& numSet) {
  if (cur.size() == maxLen) {
    int num = stoi(cur);
    if (numSet.find(num) != numSet.end()) return;
    if (che[num]) {
      numSet.insert(num);
      ans++;
    }
    return;
  }
  for (int i = 0; i < s.size(); i++) {
    if (selected[i]) continue;
    cur.push_back(s[i]);
    selected[i] = true;
    bt(maxLen, s, cur, numSet);
    cur.pop_back();
    selected[i] = false;
  }
}

int main(void) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  makeChe();

  cin >> tc;
  while (tc--) {
    ans = 0;
    fill(&selected[0], &selected[6], false);
    string cur;
    set<int> numSet;
    cin >> s;
    for (int i = 1, size = s.size(); i <= size; i++) {
      bt(i, s, cur, numSet);
    }
    cout << ans << endl;
  }

  return 0;
}

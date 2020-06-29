#include <bits/stdc++.h>

using namespace std;

bool visit[8];
set<string> s;
int ans = 0;

bool check(string user, string ban) {
  if (user.size() != ban.size()) return false;

  for (int i = 0, len = user.size(); i < len; i++) {
    if (ban[i] == '*') continue;
    if (user[i] != ban[i]) return false;
  }

  return true;
}

void dfs(vector<string>& user_id, vector<string>& banned_id, int idx) {
  if (idx == banned_id.size()) {
    string candi = "";
    // 밴된 유저들 파악
    for (int i = 0, len = user_id.size(); i < len; i++) {
      if (visit[i]) candi += user_id[i];
    }
    s.insert(candi);
    return;
  }

  string ban = banned_id[idx];
  for (int i = 0, len = user_id.size(); i < len; i++) {
    if (visit[i]) continue;
    if (!check(user_id[i], ban)) continue;

    visit[i] = true;
    dfs(user_id, banned_id, idx + 1);
    visit[i] = false;
  }
}

int solution(vector<string> user_id, vector<string> banned_id) {
  dfs(user_id, banned_id, 0);

  return s.size();
}
int main(void) {
  vector<string> user_id1({"frodo", "fradi", "crodo", "abc123", "frodoc"});
  vector<string> user_id2({"frodo", "fradi", "crodo", "abc123", "frodoc"});
  vector<string> user_id3({"frodo", "fradi", "crodo", "abc123", "frodoc"});

  vector<string> banned_id1({"fr*d*", "abc1**"});
  vector<string> banned_id2({"*rodo", "*rodo", "******"});
  vector<string> banned_id3({"fr*d*", "*rodo", "******", "******"});

  cout << solution(user_id3, banned_id3) << "\n";
  return 0;
}
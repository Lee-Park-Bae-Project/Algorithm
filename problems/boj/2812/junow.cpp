#include <bits/stdc++.h>

using namespace std;
int N, K;
string num;

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> N >> K >> num;

  int i = 0;
  int len = num.size();
  int cnt = 0;
  vector<char> ans;

  for (int i = 0; i < len; i++) {
    while (cnt < K && ans.size() > 0 && ans.back() < num[i]) {
      ans.pop_back();
      cnt++;
    }
    ans.push_back(num[i]);
  }

  int ansLen = ans.size();
  for (int i = 0; i < ansLen - (K - cnt); i++) {
    cout << ans[i];
  }

  return 0;
}
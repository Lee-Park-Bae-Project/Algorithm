#include <bits/stdc++.h>

using namespace std;
string s, b;
string f = "FRULA";

int main(void) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> s >> b;
  int i = 0;
  int slen = s.size();
  int blen = b.size();

  string t = "";
  for (int i = 0; i < slen; i++) {
    t.push_back(s[i]);

    if (t.back() == b[blen - 1]) {
      bool flag = true;
      int tlen = t.size();
      for (int j = 0; j < blen; j++) {
        if (t[tlen - j - 1] != b[blen - j - 1]) {
          flag = false;
          break;
        }
      }

      if (flag) {
        for (int j = 0; j < blen; j++) {
          t.pop_back();
        }
      }
    }
  }

  if (t.size() == 0) {
    cout << f << "\n";
  } else {
    cout << t << "\n";
  }

  return 0;
}
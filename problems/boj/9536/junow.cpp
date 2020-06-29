#include <bits/stdc++.h>

using namespace std;

int t;
vector<string> a;
string s, record;

vector<string> split(string& s) {
  istringstream ss(s);
  string sb;
  vector<string> ret;
  while (getline(ss, sb, ' ')) {
    ret.push_back(sb);
  }
  return ret;
}

string parse(string& s) {
  int i = s.find("goes") + 5;
  return s.substr(i);
}

bool check(string s) {
  for (auto _s : a) {
    if (_s == s) return false;
  }
  return true;
}
string getFox() {
  vector<string> ss = split(record);
  string fox = "";
  for (auto s : ss) {
    if (!check(s)) continue;
    fox += s + " ";
  }

  return fox;
}

int main(void) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cin >> t;

  while (t--) {
    a.clear();
    record = "";

    while (1) {
      getline(cin, s);
      if (s == "what does the fox say?") break;
      if (record.size() == 0) {
        record = s;
      } else {
        a.push_back(parse(s));
      }
    }
    cout << getFox() << "\n";
  }

  return 0;
}
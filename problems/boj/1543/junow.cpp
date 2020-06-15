#include <bits/stdc++.h>

using namespace std;

string s, t;
int i, sLen, tLen, ans;

int main(void)
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  getline(cin, s);
  getline(cin, t);
  i = 0;
  sLen = s.size();
  tLen = t.size();
  ans = 0;
  while (i < sLen)
  {
    int ni = s.find(t, i);
    if (ni < 0)
      break;
    i = ni + tLen;
    ans++;
  }
  cout << ans;
  return 0;
}
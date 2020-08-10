#include <bits/stdc++.h>
#define endl "\n"

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<pair<int, int>> vpii;

const int dy[4] = {-1, 0, 1, 0};
const int dx[4] = {0, 1, 0, -1};

struct INFO {
  int start, end;
};
struct cmp {
  bool operator()(const INFO& a, const INFO& b) {
    if ((a.end - a.start) == (b.end - b.start)) {
      return a.start > b.start;
    }

    return (a.end - a.start) > (b.end - b.start);
  }
};

int getMin(map<string, int>& m) {
  int ret = INT_MAX;
  for (auto& v : m) {
    ret = min(ret, v.second);
  }

  return ret;
}
vector<int> solution(vector<string> gems) {
  vector<int> answer;
  priority_queue<INFO, vector<INFO>, cmp> pq;
  set<string> s;
  map<string, int> m;

  for (auto& v : gems) s.insert(v);
  for (int i = 0, size = gems.size(); i < size; i++) {
    s.insert(gems[i]);
    m[gems[i]] = i + 1;
    if (m.size() != s.size()) continue;

    pq.push({getMin(m), i + 1});
  }

  answer.push_back(pq.top().start);
  answer.push_back(pq.top().end);

  return answer;
}

int main(void) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  vector<string> gems1 = {"DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"};
  vector<string> gems2 = {"AA", "AB", "AC", "AA", "AC"};
  vector<string> gems3 = {"XYZ", "XYZ", "XYZ"};
  vector<string> gems4 = {"ZZZ", "YYY", "NNNN", "YYY", "BBB"};
  vector<string> gems5 = {
      "a",
      "b",
      "b",
      "c",
      "a",
      "b",
      "c",
  };

  for (auto& v : solution(gems1)) cout << v << " ";
  cout << endl;
  for (auto& v : solution(gems2)) cout << v << " ";
  cout << endl;
  for (auto& v : solution(gems3)) cout << v << " ";
  cout << endl;
  for (auto& v : solution(gems4)) cout << v << " ";
  cout << endl;
  for (auto& v : solution(gems5)) cout << v << " ";
  cout << endl;
  return 0;
}
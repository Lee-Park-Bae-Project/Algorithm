#include <bits/stdc++.h>

using namespace std;

vector<string> ssplit(string s, char d) {
  vector<string> ret;
  stringstream ss(s);
  string temp;

  while (getline(ss, temp, d)) {
    ret.push_back(temp);
  }

  return ret;
}

string replaceSharp(string s) {
  string ret = "";
  int i = 0;
  int len = s.size();
  while (i < len) {
    if (s[i + 1] == '#') {
      ret += s[i] + 32;
      i += 2;
    } else {
      ret += s[i];
      i++;
    }
  }
  return ret;
}

int getLength(string s, string e) {
  vector<string> ss = ssplit(s, ':');
  vector<string> es = ssplit(e, ':');
  int diff = (stoi(es[0]) * 60 + stoi(es[1])) - (stoi(ss[0]) * 60 + stoi(ss[1]));
  return diff;
}

string solution(string _m, vector<string> musicinfos) {
  string answer = "";
  string m = replaceSharp(_m);
  int maxTime = 0;

  for (int i = 0, len = musicinfos.size(); i < len; i++) {
    string cur = musicinfos[i];
    vector<string> curs = ssplit(cur, ',');
    string st = curs[0];
    string et = curs[1];
    string title = curs[2];
    int length = getLength(st, et);
    string melody = replaceSharp(curs[3]);
    int melodyLen = melody.size();
    if (length < melody.size()) {
      melody = melody.substr(0, length);
    }
    // cout << st << " - " << et << " - " << title << " - " << melody << " - " << length << "\n";
    // cout << m << "\n";
    string played = "";
    // cout << m << " " << played << "\n";

    for (int j = 0; j < length; j++) {
      played += melody[j % melodyLen];
    }
    int playedLen = played.size();

    if (played.find(m) != string::npos) {
      if (maxTime < length) {
        maxTime = length;
        answer = title;
      }
    }
  }

  if (answer.size() == 0) {
    return "(None)";
  }

  return answer;
}

int main(void) {
  string m1 = "ABCDEFG";
  string m2 = "CC#BCC#BCC#BCC#B";
  string m3 = "ABC";
  vector<string> musicinfos1 = {"12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"};
  vector<string> musicinfos2 = {"03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"};
  vector<string> musicinfos3 = {"12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"};

  cout << "=======================\n";
  cout << solution(m1, musicinfos1) << "\n";
  cout << "=======================\n";
  cout << solution(m2, musicinfos2) << "\n";
  cout << "=======================\n";
  cout << solution(m3, musicinfos3) << "\n";
  return 0;
}
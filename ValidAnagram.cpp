/*
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

*/

#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <sstream>
#include <iterator>
#include <map>
#include <iomanip>
#include <utility>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <ctype.h>
#include <limits>
#include <queue>
#include <math.h>
#include <stack>

using namespace std;

class Solution {
public:
  map <char, int> getMap(string inputString) {
    map <char, int> currentMap;
    for(int i = 0; i<inputString.size(); i++){
      if (currentMap[inputString[i]]) {
        currentMap[inputString[i]]++;
      } else {
        currentMap[inputString[i]] = 1;
      }
    }
    return currentMap;
  }

  bool isAnagram(string s, string t) {
    map <char, int> myMapS = getMap(s);
    map <char, int> myMapT = getMap(t);
    if (s.size() != t.size()){
      return false;
    } else if (myMapS.size()!= myMapT.size()) {
      return false;
    } else {
      for (map<char,int>::iterator it=myMapS.begin(); it!= myMapS.end(); ++it){
        if (!myMapT[it->first]) {
          return false;
        }
        if (myMapS[it->first] != myMapT[it->first]) {
          return false;
        }
      }
      return true;
    }

  }
};
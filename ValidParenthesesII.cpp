/*
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


This is the version that using recurrsive calls, but this is not efficient and I reached the time limit on leetcode
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
    bool isValid(string s) {
        stack<char> mystack;
        for (int i=0; i<s.size(); i++){
          char cur_chr=s[i];
          if (cur_chr=='(' | cur_chr=='[' | cur_chr=='{'){
            mystack.push(cur_chr);
          }
          else if (cur_chr==')'){
            if(!mystack.empty() && mystack.top()=='(') mystack.pop();
            else return false;
          }
          else if (cur_chr==']'){
            if(!mystack.empty() && mystack.top()=='[') mystack.pop();
            else return false;
          }
          else if (cur_chr=='}'){
            if(!mystack.empty() && mystack.top()=='{') mystack.pop();
            else return false;
          }
          else if (mystack.empty()) {} ;
        }

        if(!mystack.empty()) return false;
        else return true;
    }
};




int main(){  
  Solution sol;  
  cout<<sol.isValid("")<<endl<<endl;
  cout<<sol.isValid("[   ")<<endl<<endl;
  cout<<sol.isValid("[   ]   ")<<endl<<endl;
  cout<<sol.isValid("(  [{}])")<<endl<<endl;
  cout<<sol.isValid("  ()   [   ]   ")<<endl<<endl;
  cout<<sol.isValid("({]])]})]}([)}{][)]{}{(])}([]}])})}([]}({}([{][{}")<<endl<<endl;
  
}











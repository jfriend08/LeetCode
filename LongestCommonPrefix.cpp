/*
Write a function to find the longest common prefix string amongst an array of strings.

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
    string longestCommonPrefix(vector<string> &strs) {
        if (strs.size()==0) return "";
        else if (strs.size()==1) return strs[0];

        string result="", tmp="";
        for (int i=0; i<strs[0].size(); i++){
          
          tmp.push_back(strs[0][i]);          
          // cout<<"iterate:"<<i<<" current tmp:"<<tmp<<endl;

          for (int j=1; j<strs.size(); j++){
            // cout<<"j:"<<j<<" current sub string: "<<strs[j].substr(0,i+1)<<endl;
            if(tmp != strs[j].substr(0,i+1) ) return result;
          }          
          result=tmp;
        }
        return result;
    }
};



int main(){  
  Solution sol;  
  vector<string> input;
  // input.push_back("a");
  // input.push_back("a");
  // input.push_back("b");
  cout<<sol.longestCommonPrefix(input)<<endl;
  
  
}











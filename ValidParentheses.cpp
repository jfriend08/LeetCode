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

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        map <char, int> mymap;
        mymap['(']=1;mymap[')']=1;mymap['[']=2;mymap[']']=2;mymap['{']=3;mymap['}']=3;
        
        bool hasParentheses=false;
        // cout<<s<<endl;
        for (int i=0; i<s.size(); i++){                    
          if (mymap[s[i]]){
            // cout<<"found parentheses"<<endl;
            hasParentheses=true;
            // cout<<mymap[s[i]]<<endl;
            int left =i, right=i+1;
            for (int j =i+1; j<s.size(); j++){            
              if (mymap[s[left]] == mymap[s[j]]) {
                right=j;                
                if(isValid(s.substr(left+1,right-left-1)) && isValid(s.substr(right+1,s.size()-right-1))) return true;
              }
            }
            // cout<<left<<" "<<right<<endl;
            // cout<<"left:"<<s[left]<<" right:" << s[right]<<endl;

            if ( s[left]==s[right] | mymap[s[left]] != mymap[s[right]]) return false;
            else return isValid(s.substr(left+1,right-left-1)) && isValid(s.substr(right+1,s.size()-right-1));
          }
        }
        // cout<<"hasParentheses? "<<hasParentheses<<endl;
        return hasParentheses ? false:true;
    }
};




int main(){  
  Solution sol;
  // cout<<sol.isValid("( {)")<<endl<<endl;
  // cout<<sol.isValid("( )")<<endl<<endl;
  // cout<<sol.isValid("( ) []")<<endl<<endl;
  // cout<<sol.isValid("( ) {[]}")<<endl<<endl;
  // // cout<<sol.isValid("( (")<<endl<<endl;
  // cout<<sol.isValid("[({(())}[()])]")<<endl<<endl;
  // cout<<sol.isValid("{}{{}}")<<endl<<endl;
  cout<<sol.isValid("({]])]})]}([)}{][)]{}{(])}([]}])})}([]}({}([{][{}")<<endl<<endl;
  
  
  
  
}




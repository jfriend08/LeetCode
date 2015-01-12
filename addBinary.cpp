/*
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

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
    string addBinary(string a, string b) {
      string result;
      int i=a.size()-1;
      int j=b.size()-1;
      int limitSize= a.size()<b.size() ? a.size():b.size();
      int carry=0;
      char buffer;

      for (int i=0; i<limitSize;i++){        
        int tmp=(a[a.size()-1-i]-'0'+b[b.size()-1-i]-'0'+carry)%2;
        // cout<<"tmp:"<<tmp<<endl;
        carry=(a[a.size()-1-i]-'0'+b[b.size()-1-i]-'0'+carry)/2;        
        result.insert(0,to_string(tmp));
      }      

      if (a.size()>b.size()){
        for (int i=0; i<a.size()-b.size(); i++){
          int tmp=(a[a.size()-1-b.size()-i]-'0'+carry)%2;        
          carry=(a[a.size()-1-b.size()-i]-'0'+carry)/2;        
          result.insert(0,to_string(tmp));
        }        
      }
      else if (a.size()<b.size()){
        for (int i=0; i<b.size()-a.size(); i++){
          int tmp=(b[b.size()-1-a.size()-i]-'0'+carry)%2;        
          carry=(b[b.size()-1-a.size()-i]-'0'+carry)/2;        
          result.insert(0,to_string(tmp));
        }        
      }

      if (carry==1){      
        result.insert(0,"1");
      }

      return result ;
    }
    
};

int main(){  
  vector<int> input, output;
  Solution sol;
  cout<<sol.addBinary("100", "1010")<<endl;
  cout<<sol.addBinary("1010", "100")<<endl;
  cout<<sol.addBinary("1010", "110")<<endl;
  
  
  
  
}




/*
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

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
#include <cstdlib>
#include <stack> 

using namespace std;

class Solution {
public:
    string convert(string s, int nRows) {
        // vector of vector will be 196 ms
        // vector<vector <char> > mytable(nRows);
        
        // vector of string will be 128 ms
        vector<string> mytable(nRows);

        int level=0, direction=1;
        string convert_str="";

        if (nRows<=1) return s;
        for (int i=0; i<s.length(); i++){
          // cout<<"direction:"<<direction<<"\t"<<"level: "<<level<<endl;
          mytable[level]+=s[i];
          // mytable[level].push_back(s[i]);
          direction == 1 ? level++ : level-- ;
          if (level ==0 | level ==nRows-1) direction=direction*(-1);
        }

        for (int j=0; j<nRows; j++){
          
          convert_str+=mytable[j];  
          // // vector of vector
          // for (int k=0; k<mytable[j].size(); k++){
          //   convert_str+=mytable[j][k];  
          // }
          
          
        }
        return convert_str;
    }
};


int main(){
  Solution sol;
  string mystring="PAYPALISHIRING";
  cout<<sol.convert(mystring, 3)<<endl;


}









/*
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
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
    int romanToInt(string s) {
      map<char, int> myMAP;
      myMAP['I']=1;myMAP['V']=5;myMAP['X']=10;myMAP['L']=50;myMAP['C']=100;myMAP['D']=500;myMAP['M']=1000;
      int curMax=0, idx, result=0;
      if (s.size()==0) return 0;
      else if (s.size()==1) return myMAP[s[0]];

      for (int i=0; i<s.size(); i++){
        if (myMAP[s[i]]>curMax){curMax=myMAP[s[i]]; idx=i;}
      }
      // cout<<s.substr(idx+1, s.size()-idx)<<endl;
      return curMax+romanToInt(s.substr(idx+1, s.size()-idx))-romanToInt(s.substr(0, idx));
      
      // return curMax;
    }
};




int main(){  
  Solution sol;
  
  cout<<"I:"<<sol.romanToInt("I")<<endl;
  cout<<"II:"<<sol.romanToInt("II")<<endl;
  cout<<"IV:"<<sol.romanToInt("IV")<<endl;
  cout<<"VI:"<<sol.romanToInt("VI")<<endl;
  cout<<"X:"<<sol.romanToInt("X")<<endl;
  cout<<"XII:"<<sol.romanToInt("XII")<<endl;
  cout<<"XXXII:"<<sol.romanToInt("XXXII")<<endl;
  cout<<"XXXIX:"<<sol.romanToInt("XXXIX")<<endl;
  cout<<"XL:"<<sol.romanToInt("XL")<<endl;
  cout<<"LX:"<<sol.romanToInt("LX")<<endl;
  cout<<"XCIV:"<<sol.romanToInt("XCIV")<<endl;

  
}






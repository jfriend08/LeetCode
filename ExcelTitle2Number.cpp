/*
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB

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
private:
  int findLetter(char* array, char c){
    for (int i=0; i<26; i++){
      if (array[i]==c) return i==0 ? 26:i;      
    }
    return 26;
  }
public:
    int titleToNumber(string s) {
      char letter[]={'Z','A', 'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y'};        
      vector<int> numV;
      int num=0;
      for (int i=0; i<s.length(); i++){
        num+=pow(26,s.length()-1-i)*findLetter(letter, s[i]);
      }      
      return num;
    }
};

int main(){
  
  Solution sol;
  
  cout<<sol.titleToNumber("A")<<endl;
  cout<<sol.titleToNumber("B")<<endl;
  cout<<sol.titleToNumber("BB")<<endl;
  cout<<sol.titleToNumber("ZZ")<<endl;
  cout<<sol.titleToNumber("AAA")<<endl;
  cout<<sol.titleToNumber("ABU")<<endl;
  
}




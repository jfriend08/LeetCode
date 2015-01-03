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

using namespace std;

class Solution {

public:
    string convertToTitle(int n) {
        char letter[]={'Z','A', 'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y'};
        div_t result=div(n, 26);
        string columnLetter;
        
        // in general, the columnLetter= convertToTitle(result.quot) + letter[result.rem]
        // which means, is the result.quot is begger than 26, then it will continue the works recurrsively

        // for the case that n<=26, just use n as index to find value in letter array
        if (n<=26){columnLetter=letter[result.rem];}
        
        // e.g. n=52, quot=2 and rem=0. it should be AZ. so we should put quot-1 into the recurrsive call
        else if (result.rem==0){
          columnLetter+=convertToTitle(result.quot-1);
          columnLetter+=letter[result.rem];  
        }
        // e.g. n=53, quot=2 and rem=1. it should be BA. so it is ok to directly put quot into recurrsive call
        else{
          columnLetter+=convertToTitle(result.quot);
          columnLetter+=letter[result.rem];  
        }    

        return columnLetter;
    }
};

int main(){
  int input = 52;
  Solution sol;
  // cout<<sol.convertToTitle(input)<<endl;
  for (int i =51; i<56; i++){
    cout<<i<<": "<<sol.convertToTitle(i)<<endl;
  }

  for (int i =675; i<750; i++){
    cout<<i<<": "<<sol.convertToTitle(i)<<endl;
  }
  

}




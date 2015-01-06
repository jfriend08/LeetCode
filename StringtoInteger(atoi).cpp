/*
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

spoilers alert... click to show requirements for atoi.

Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

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
#include <limits.h>

using namespace std;
class Solution {
public:
    
    int atoi(const char *str) {
        bool pos=true;
        int val=0, idx=0;
        while (str[idx] == ' ') idx++;
        
        if (str[idx] == '+') {pos=true; idx++;}
        else if (str[idx] == '-') {pos=false; idx++;}

        while (str[idx]>='0' && str[idx]<='9'){          
          if ( val>INT_MAX/10  || (val==INT_MAX/10 && str[idx] -'0'> 7) ) {            
            return pos ? INT_MAX : INT_MIN;
          }
          val=val*10+str[idx]-'0';                    
          // cout<<idx<<":"<<val<<endl;                    
          idx++;
        }        
        
        return pos ? val : -val;
    }
};


int main(){
  Solution sol;  
  cout <<sol.atoi("2147483646")<<endl;
  cout <<sol.atoi("2147483647")<<endl;
  cout <<sol.atoi("2147483648")<<endl;
  cout <<sol.atoi("2147483650")<<endl;
  cout <<sol.atoi("2147483750")<<endl;

  cout <<sol.atoi("-2147483646")<<endl;
  cout <<sol.atoi("-2147483647")<<endl;
  cout <<sol.atoi("-2147483648")<<endl;
  cout <<sol.atoi("-2147483649")<<endl;
  // cout <<sol.atoi("    2147483649")<<endl;
  // cout <<sol.atoi("    2147483649")<<endl;
}










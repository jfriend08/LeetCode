/*
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.

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
    int lengthOfLastWord(const char *s) {
      bool bit;
      int length=0, tmp=0;
      while (*s){      
        if(*s != ' ') {          
          s++;
          if(bit){length=0; bit= false;}
          length++;          
        }
        else if(*s == ' '){                    
          s++;
          bit=true;
        }
        
      }
      return length;
    }
};




int main(){  
  Solution sol;
  cout<<sol.lengthOfLastWord("hello hoho")<<endl;
  cout<<sol.lengthOfLastWord("hello")<<endl;
  cout<<sol.lengthOfLastWord("")<<endl;
  cout<<sol.lengthOfLastWord("a ")<<endl;
  cout<<sol.lengthOfLastWord("b   a    ")<<endl;
}




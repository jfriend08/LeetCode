/*
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.

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
#include <ctype.h>
#include <math.h>

using namespace std;
class Solution {
public:
    bool isPalindrome(int x) {          
     if (x<0) return false;   
     vector<int> myvector;
     while (x!=0){
      myvector.push_back(x%10);
      x=x/10;
     }
     for (int i=0; i<myvector.size();i++){
      // cout<<myvector[i]<<" vs "<<myvector[myvector.size()-i-1]<<endl;
      if(myvector[i]!=myvector[myvector.size()-i-1])return false;      
     }
     // cout<<endl;
     return true;
    }
};

int main(){
  Solution sol;  
  cout<<sol.isPalindrome(1)<<endl;
  cout<<sol.isPalindrome(9)<<endl;
  cout<<sol.isPalindrome(-1)<<endl;
  
  cout<<sol.isPalindrome(1234321)<<endl;
  cout<<sol.isPalindrome(101)<<endl;
  cout<<sol.isPalindrome(102)<<endl;
  cout<<sol.isPalindrome(100001)<<endl;
  cout<<sol.isPalindrome(1000021)<<endl;

}










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
     cout<<"x:"<<x<<endl;
     if (x<0) return false;   
     else if (x==0) return true;

     int count=0, oper=x;
     int last_digit=x%10;

     while(oper>=10){
	    oper=oper/10;	 
     	count++;
     }
     
     if (x<=9 && x>=1) return true;
     else if (oper== last_digit) {
     	int next= (x-oper*pow(10,count))/10;
     	return isPalindrome(next);
     }
     else return false;

    }
};

int main(){
  Solution sol;  
  // cout<<sol.isPalindrome(1)<<endl;
  // cout<<sol.isPalindrome(9)<<endl;
  // cout<<sol.isPalindrome(-1)<<endl;
  // cout<<sol.isPalindrome(1234321)<<endl;
  // cout<<sol.isPalindrome(101)<<endl;
  // cout<<sol.isPalindrome(102)<<endl;
  // cout<<sol.isPalindrome(100001)<<endl;
  cout<<sol.isPalindrome(1000021)<<endl;

}










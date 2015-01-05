/*
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

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
#include <math.h>

using namespace std;

class Solution {
private:
  vector<int> rev_int;
  
  // it will save every digit into vector reversely
  // e.g. 123: rev_int[0]->3, rev_int[1]->2, rev_int[2]->1
  void put2vector(int x){
    int digit=x %10;
        rev_int.push_back(digit);
        if (x >=10)
          put2vector(x/10);
  }

public:    
    int reverse(int x) {
      
      // forget whether x is pos or neg, just put its abs into pur2vector
      if(x>=0) put2vector(x);
      else if(x<0) put2vector(x*-1);
      
      // add up each digits with proper mutiplication, and save to myvalue
      int myvalue=0;      
      for (int i=0; i<rev_int.size(); i++){
        myvalue+=+rev_int[i]*pow(10,rev_int.size()-i-1);
      }
      rev_int.clear();

      // if it is overflow, the sign of the value will be differ than the original input x
      if (x>=0 && myvalue<0) return 0;  // overflow case
      else if (x<0 && myvalue<0) return 0; // overflow case
      else
        return (x>=0 ? myvalue : myvalue*-1);  // normal case
    }
};


int main(){
  Solution sol;
  cout<<sol.reverse(123)<<endl;
  cout<<sol.reverse(100)<<endl;
  cout<<sol.reverse(-123)<<endl;
  cout<<sol.reverse(1534236469)<<endl;
  cout<<sol.reverse(-1534236469)<<endl;
}









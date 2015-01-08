/*
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

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
#include <math.h> 

using namespace std;
class Solution {
public:
    int trailingZeroes(int n) {

      return n > 0 ? (floor(n/5) + trailingZeroes(n/5)): 0;      
    }
};

int main(){
  Solution sol;  
  cout<<sol.trailingZeroes(32)<<endl;
}
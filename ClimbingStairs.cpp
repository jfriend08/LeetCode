/*
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

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
    map<int,int> mymap;
    
    int climbStairs(int n) {
        if (n==1) {mymap[n]=1;return 1;}            
        else if (n==2) {mymap[n]=2;return 2;}
        else {
            int option1, option2;
            if (mymap.find(n-1)!=mymap.end()) {option1=mymap[n-1];}
            else option1= climbStairs(n-1);
            
            if (mymap.find(n-2)!=mymap.end()) {option2=mymap[n-2];}
            else option2= climbStairs(n-2);            
            
            mymap[n]=option1+ option2;
            return(option1+ option2);
        }
    }
};


int main(){  
  Solution sol;
  cout<<sol.climbStairs(1)<<endl;
  cout<<sol.climbStairs(2)<<endl;
  cout<<sol.climbStairs(3)<<endl;
  cout<<sol.climbStairs(4)<<endl;
  cout<<sol.climbStairs(5)<<endl;
  cout<<sol.climbStairs(44)<<endl;
  
}




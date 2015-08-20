/*
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

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
#include <stack>

using namespace std;

class Solution {
public:
    // the key idea for this method is: if two value is the same, the XOR is 0, a^a =0
    int singleNumber(int A[], int n) {
        int val=A[0];
        for (int i=1; i<n; i++){
            val ^= A[i];
        }
        return val;
        
    }
};









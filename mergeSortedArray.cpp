/*
Given two sorted integer arrays A and B, merge B into A as one sorted array.

Note:
You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. 
The number of elements initialized in A and B are m and n respectively.

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
    void merge(int A[], int m, int B[], int n) {
     int idx=m+n-1;
     int i=m-1, j=n-1;
     
     while (i>=0 && j>=0){
         if (A[i]>=B[j]) A[idx--]=A[i--];
         else A[idx--]=B[j--];
     }
     while(j>=0){
         A[idx--]=B[j--];
     }
     
    }
};




int main(){  
  Solution sol;
  
}




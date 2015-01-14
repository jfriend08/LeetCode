/*
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

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
    int removeDuplicates(int A[], int n) {
        if(n ==0) return 0;
        if(n ==1) return 1;        
        int i=0, j=i+1;
        for (;j<n; j++){            
            if(A[i]==A[j]){}
            else A[++i]=A[j];
        }
        return i+1;
    }
};




int main(){  
  Solution sol;
  int A[] = {1,1,2};
  cout<<sol.removeDuplicates(A, 3)<<endl;
  
}




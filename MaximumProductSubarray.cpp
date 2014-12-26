/*
Find the contiguous subarray within an array (containing at least one number) which has the largest product.
For example, given the array [2,3,-2,4], the contiguous subarray [2,3] has the largest product = 6.

Tag: Array, Dynamic Programming

Note: this just don't work

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

using namespace std;

class Solution {
private:
	struct localMaxMin{
		int max;
		int min;		
	};

  int largest(int a, int b, int c){
    int max = a;
    if (b > max) max = b; 
    if (c > max) max = c;
    return max;
  }
  int smallest(int a, int b, int c){
    int min = a;
    if (b < min) min = b; 
    if (c < min) min = c;
    return min;
  }

  localMaxMin submax(int A[], int start, int upperbound, localMaxMin current){
    localMaxMin local;local.max= A[start];
    
    if (start == upperbound-1){local.min=A[start];}
    
    else{
      int tmp1 = A[start] * current.max;
      int tmp2 = A[start] * current.min;
      local.max=largest(tmp1, tmp2, A[start]);
      local.min=smallest(tmp1, tmp2, A[start]);
    }
    return local;
  }

public:
	int maxProduct(int A[], int n) {
  	int maxproduct= -2147483648; // this is the real/global max product; initialized to the smallest value of int
  	localMaxMin local; // this is the local max product, but may not be global max    
    for (int i=n; i --> 0; ){    
      local=submax(A, i, n, local); // input current localmax, and then update localmax
      if (local.max> maxproduct){ maxproduct= local.max;}      
    }  		
    return maxproduct;
	}
};



int main() {
	int A[3] = {-4,-3,-2};
	Solution myclass;
	int result= myclass.maxProduct(A, 3);
	cout<<result<<endl;
	return 0;
}






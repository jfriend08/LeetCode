/*
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

click to show spoilers.

Note:
Your solution should be in logarithmic complexity.

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
    int findPeakElement(const vector<int> &num) {
        int l=0;
        int h=num.size()-1;
        while(h>l){
            int m=(l+h)/2;
            if (num[m] < num[m+1])
                l=m+1;
            else 
                h=m;
        }
        return l;
        
    }
};

int main(){
	Solution q;
	vector<int> v;
	v.push_back(1);v.push_back(2);v.push_back(3);v.push_back(1);
	cout<<q.findPeakElement(v)<<endl;
}
/*
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

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
    int majorityElement(vector<int> &num) {
    	int major, vectorsize=num.size(), bound= vectorsize/2;        
        for (int count=0, i=0; i<vectorsize && count<=bound; i++){
            if (count==0){
                major= num[i];
                count++;
            }
            else major == num[i] ? count++ : count--;
        }
        return major;
    }
};


int main(){
	vector<int> myvector;
	for (int i=1; i<=5; i++) myvector.push_back(i);
	myvector.push_back(10);myvector.push_back(10);myvector.push_back(10);myvector.push_back(10);myvector.push_back(10);myvector.push_back(10);

	Solution sol;
	int myreturn= sol.majorityElement(myvector);
	cout<<myreturn<<endl;


}







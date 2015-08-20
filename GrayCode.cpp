/*
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. 
A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.

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
    int binary2gray(int bi){
        int val=bi>>1;
        cout<<"out:"<<val<<" bi:"<<bi<<endl;
        return (bi>>1)^bi ;
    }

    vector<int> grayCode(int n) {
        vector<int> result;
        // result.push_back(0);        

        for (int i=0; i<pow(2,n); i++){            
            result.push_back(binary2gray(i));
        }
        return result;
    }
};


int main(){

    Solution s;
    vector<int> v=s.grayCode(3);
    for (int i =0; i<v.size(); i++){
        cout<<v[i]<<endl;
    }
}





















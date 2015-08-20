/*
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)

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
    vector<vector<int> > threeSum(vector<int> &num) {        
        vector<vector<int> > result;
        map<vector<int>,int> mymap;
        if(num.size()<3) return result;
        sort(num.begin(), num.end());
        int Twosum;
        for (int i=0; i<num.size()-2;){
            int l=i+1, r=num.size()-1;
            Twosum=0-num[i];
            while(l<r){
                if (num[l]+num[r]<Twosum) l++;
                else if (num[l]+num[r]==Twosum){
                    vector<int> v;                    
                    v.push_back(num[i]);v.push_back(num[l]);v.push_back(num[r]);
                    // if(!mymap[v]){
                        result.push_back(v);
                        // mymap[v]=1;
                    // }
                    do{l++;} while (l<r && num[l]==num[l-1]);
                    do{r--;} while (l<r && num[r]==num[r+1]);
                }
                else r--;
            }
            do{i++;} while (i<num.size() && num[i]==num[i-1]);
        }
        sort(result.begin(), result.end());
        return result;
    }
};


int main(){
    Solution sol;
    vector<int> input;
    vector<vector<int> > output;
    input.push_back(-1);input.push_back(0);input.push_back(1);input.push_back(2);input.push_back(-1);input.push_back(-4);

    output=sol.threeSum(input);
    for (int i=0; i<output.size();i++){
        for (int j=0;j<output[i].size();j++){
            cout<<output[i][j];
        }
        cout<<endl;
    }

}





















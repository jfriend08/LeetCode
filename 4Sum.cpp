/*
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
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
#include <limits.h>

using namespace std;

class Solution {
public:
    vector<vector<int> > fourSum(vector<int> &num, int target) {
        vector<vector<int> > result;
        if(num.size()<4) return result;
        sort(num.begin(), num.end());
        // printV(num); cout<<"target:"<<target<<endl;

        for(int i=0; i<num.size()-3; ){            
            for(int j=num.size()-1; j>=i+3; ){                
                int TwoSum=target-num[i]-num[j];
                int left=i+1; // next to i
                int right=j-1; // rightmost index - i -1 (next to it)
                
                while(left<right){
                    // cout<<"TwoSum:"<<TwoSum<<" i:"<<i<<" left:"<<left<<" right:"<<right<<" j:"<<j<<endl;
                    if(num[left]+num[right]==TwoSum){
                        vector<int> myV;                    
                        cout<<num[i]<<" "<<num[left]<<" "<<num[right]<<" "<<num[j]<<endl;
                        myV.push_back(num[i]);myV.push_back(num[left]);myV.push_back(num[right]);myV.push_back(num[j]);
                        result.push_back(myV);
                        do{right--;}while(num[right]==num[right+1]);
                        do{left++;}while(num[left]==num[left-1]);
                    }
                    
                    if(num[left]+num[right]<TwoSum)
                        left++;                    
                    else if(num[left]+num[right]>TwoSum)
                        right--;                    
                }
                do{j--;}while(num[j]==num[j+1]);
            }do{i++;}while(num[i]==num[i-1]);
        }
        return result;
        
    }
    
    void printV(vector<int> v){
        for (int i=0; i<v.size(); i++){
            cout<<v[i]<<" ";
        }
        cout<<endl;
    }
};


int main(){
    Solution sol;
    vector<int> input;
    vector<vector<int> > output;
    // input.push_back(1);input.push_back(0);input.push_back(-1);input.push_back(0);input.push_back(-2);input.push_back(2);
    // sol.fourSum(input, 0);
    // input.push_back(1);input.push_back(0);input.push_back(-1);input.push_back(0);input.push_back(-2);input.push_back(2);
    // sol.fourSum(input, 0);
    input.push_back(5);input.push_back(5);input.push_back(3);input.push_back(5);input.push_back(1);input.push_back(-5);input.push_back(1);input.push_back(2);
    sol.fourSum(input, 4);
    

}





















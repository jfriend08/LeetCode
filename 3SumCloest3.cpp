/*
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. 
You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

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
    int threeSumClosest(vector<int> &num, int target) {
        sort(num.begin(), num.end());
        // printV(num);cout<<"target:"<<target<<endl;
        int ABScloestNum=INT_MAX;
        int Answer;
        
        for(int i=0; i<num.size()-2; i++){
            int remain=target-num[i];
            int left=i+1, right=num.size()-1;        
            
            while(left<right){
                int curSum=num[i]+num[left]+num[right];
                if( abs(curSum-target)<ABScloestNum ){
                    ABScloestNum=abs(curSum-target);
                    Answer=curSum;
                }

                if(curSum>target){
                    right--;
                }
                else{
                    left++;
                }
            }
        }
        return Answer;
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
    input.push_back(1);input.push_back(2);input.push_back(4);input.push_back(8);input.push_back(16);input.push_back(32);input.push_back(64);input.push_back(128);
    // input.push_back(-1);input.push_back(2);input.push_back(1);input.push_back(-4);

    sol.threeSumClosest(input,82);
    // cout<<sol.threeSumClosest(input,1)<<endl;
    

}





















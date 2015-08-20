/*
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. 
You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.
    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

This is brute force. should be correct but reach time limit

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
        vector<vector<int> > myResult;

        sort(num.begin(), num.end());
        for(int i=0; i<num.size()-2; i++){
            vector<int> curV;
            int TwoSUM=target-num[i];
            int l=i+1, r=num.size()-1;
            if (num[l]+num[r]==TwoSUM) {return target;}
            // too big, trying to minimize TwoSUM
            else if (num[l]+num[r]>TwoSUM){
                cout<<"too big"<<endl;
                int diff=INT_MAX;                
                do{
                    diff=abs(num[l]+num[r]-TwoSUM);
                    r--;                    
                }while(l<r && abs(num[l]+num[r]-TwoSUM)<diff);
                
            }
            // too small, trying to maxminize TwoSUM
            else if (num[l]+num[r]<TwoSUM) {
                cout<<"too small"<<endl;
                int diff=INT_MAX;               
                do{
                    diff=abs(num[l]+num[r]-TwoSUM);                                        
                    l++;                    
                }while(l<r && abs(num[l]+num[r]-TwoSUM)<diff);
                
            }
            cout<<"l:"<<l<<" r:"<<r<<endl;
            cout<<num[i]<<" "<<num[l]<<" "<<num[r]<<endl;
            curV.push_back(num[i]);curV.push_back(num[l]);curV.push_back(num[r]);            
            myResult.push_back(curV);
        }
        return cloest(myResult, target);
    }
    
    int cloest(vector<vector<int> > vv, int target){
        long cloestNum=INT_MAX, cur_num;
        for (int i=0; i<vv.size(); i++){            
            cur_num=vv[i][0]+vv[i][1]+vv[i][2];            
            if (cur_num==target) return target;
            if (abs(cur_num-target)<=abs(cloestNum-target)) cloestNum=cur_num;
            // cout<<cloestNum<<endl;
        }
        return cloestNum;
    }
};


int main(){
    Solution sol;
    vector<int> input;
    vector<vector<int> > output;
    input.push_back(1);input.push_back(2);input.push_back(4);input.push_back(8);input.push_back(16);input.push_back(32);input.push_back(64);input.push_back(128);

    cout<<sol.threeSumClosest(input,82)<<endl;
    

}





















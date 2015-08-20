/*
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. 
You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

This one is buggy

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
        vector<vector<int> > result;
        
        sort(num.begin(), num.end());
        // printV(num);
        for (int i=0; i<num.size()-2; i++){
            int TwoSum=target-num[i];
            int left=i+1, right=num.size()-1;
            int curdiff=abs(TwoSum-num[left]-num[right]);
            bool change;
            // cout<<"target:"<<target<<" curdiff:"<<curdiff<<endl;
            do{
                change=true; 
                int orginal_left=left, orginal_right=right;
                // cout<<"In while loop  i: "<<i<<" left:"<<left<<" right:"<<right<<endl;
                if(left+1<right && abs(TwoSum-num[left+1]-num[right])<curdiff ){
                    left++;
                    curdiff=abs(TwoSum-num[left]-num[right]);
                    // cout<<"left new diff:"<<curdiff<<endl;
                }
                else if(left<right-1 && abs(TwoSum-num[left]-num[right-1])<curdiff ){
                    right--;
                    curdiff=abs(TwoSum-num[left]-num[right]);
                    // cout<<"right new diff:"<<curdiff<<endl;
                }
                else {
                    change=false; 
                }
            }while(left<right && change);
            

            // cout<<"i: "<<i<<" left:"<<left<<" right:"<<right<<endl;
            // cout<<num[i]<<" "<<num[left]<<" "<<num[right]<<endl;
            vector<int> myV;
            myV.push_back(num[i]);myV.push_back(num[left]);myV.push_back(num[right]);
            result.push_back(myV);

        }

        return cloest(result, target);
        
    }
    void printV(vector<int> v){
        for(int i=0; i<v.size(); i++){
            cout<<v[i]<<" ";
        }
        cout<<endl;
    }
    
    int cloest(vector<vector<int> > vv, int target){
        long cloestNum=INT_MAX, cur_num;
        for (int i=0; i<vv.size(); i++){            
            cur_num=vv[i][0]+vv[i][1]+vv[i][2];            
            if (cur_num==target) return target;
            if (abs(cur_num-target)<=abs(cloestNum-target)) cloestNum=cur_num;            
     
     This one is buggy
        }
        return cloestNum;
    }
};


int main(){
    Solution sol;
    vector<int> input;
    vector<vector<int> > output;
    // input.push_back(1);input.push_back(2);input.push_back(4);input.push_back(8);input.push_back(16);input.push_back(32);input.push_back(64);input.push_back(128);
    input.push_back(-1);input.push_back(2);input.push_back(1);input.push_back(-4);

    // sol.threeSumClosest(input,82);
    cout <<sol.threeSumClosest(input,1)<<endl;
    

}





















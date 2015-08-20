/*
The answer is correct, but time limit will exceed

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
private:
    vector<vector<int> > result;
    vector<int> myvector;
    map<vector<int>,int > mymap;
    int a,b,c;
public:
    vector<vector<int> > threeSum(vector<int> &num) {        
        for(int i=0; i<num.size();i++){
            a=num[i];myvector.push_back(a);
            for (int j=i+1; j<num.size();j++){            
                b=num[j];myvector.push_back(b);
                for(int k=j+1; k<num.size();k++){        
                    c=num[k];myvector.push_back(c);
                    if(isValid(myvector)) {result.push_back(myvector);}   
                    myvector.pop_back(); 
                }                    
                myvector.pop_back(); 
            }
            myvector.pop_back(); 
        }
        return result;
    }

    bool isValid(vector<int> v){        
        Sort(v[0],v[1],v[2]);
        if(v[0]+v[1]+v[2]==0 && mymap[v]!=1){
            mymap[v]=1;
            return true;
        }
        return false;        
    }

    void Sort(int &a, int &b, int &c){        
        if(a>b){
            int tmp = a;
            a = b;
            b = tmp;
        }
        if(a>c){
            int tmp = a;
            a=c;
            c = tmp;
        }
        if(b>c){
            int tmp = b;
            b=c;
            c=tmp;
        }
        return;
    }

    void printV(vector<int> v){
        for(int i=0; i<v.size(); i++) cout<<v[i]<<"_";
        cout<<endl;
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





















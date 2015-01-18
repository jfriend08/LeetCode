/*
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). 
You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.

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
    void printV(vector<int> v){
        for (int i=0; i<v.size(); i++){
            cout<<v[i]<<" ";
        }
        cout<<endl;
    }
public:
    int canCompleteCircuit(vector<int> &gas, vector<int> &cost) {
        printV(gas);printV(cost);
        if (gas.size()==1) {return gas[0]>=cost[0] ? 0:-1;}
        else if (gas.size()==0) return -1;
        
        for (int i=0; i<gas.size(); i++){
            int tank=0, count=0;
            // cout<<"i:"<<i<<endl;
            // start the travel from station i
            while(tank>=0 && count<=gas.size()){
                cout<<"i:"<<i<<" current tank:"<<tank<<" Count:"<<count<<endl;
                tank+= gas[(i+count)%gas.size()];
                tank-=cost[(i+count)%gas.size()];
                count+=1;
            }
            
            if (count==gas.size()+1) return i;
            else {
                cout<<"start at:"<<i<<" fail at gas"<<i+count<<endl;
                i=i+count-1;
            }
            
        }
        return -1;
    }
};



int main(){  
  Solution sol;   
  int gas[] = {2,4};
  int cost[] = {3,4};
  vector<int> gasV (gas, gas+sizeof(gas)/sizeof(int) );
  vector<int> costV (cost, cost+sizeof(cost)/sizeof(int) );
  cout<<sol.canCompleteCircuit(gasV, costV)<<endl;

}











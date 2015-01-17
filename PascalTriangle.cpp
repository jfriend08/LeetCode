/*
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

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
#include <cstdlib>

using namespace std;



class Solution {
private:
    void printVector(vector<int> v){
        for (int i=0; i<v.size();i++){
            cout<<v[i]<<" ";
        }
        cout<<endl;
    }

public:
    vector<vector<int> > generate(int numRows) {
        vector<vector<int> > result;
        vector<int> myvector, myprevious;

        for (int i=1; i<=numRows; i++){
            if (i==1){myvector.push_back(1);}
            else if (i==2){myvector.push_back(1);myvector.push_back(1);}
            else{
                myvector.push_back(1);
                for (int j=0; j<myprevious.size()-1; j++){                    
                    myvector.push_back(myprevious[j]+myprevious[j+1]);
                }
                myvector.push_back(1);
            }
            // printVector(myvector);
            myprevious=myvector;            
            result.push_back(myvector);
            myvector.clear();
        }
        return result;

    }
};


int main(){  
  Solution sol;    
  vector<vector<int> > v=sol.generate(5);

  for(int i =0; i<=v.size()-1; i++){
    for (int j=0; j<v[i].size();j++){
        cout<<v[i][j]<<" ";
    }
    cout<<endl;
  }  
}










/*
Compare two version numbers version1 and version1.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:
0.1 < 1.1 < 1.2 < 13.37

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
public:
    vector<int> getRow(int rowIndex) {
        vector<int> myvector;
        vector<int> tmpV;        
        myvector.push_back(1);        
        if (rowIndex == 0) {}    
        else{            
            tmpV=getRow(rowIndex-1);                        
            if (tmpV.size()<2){
                myvector.insert(myvector.end(), tmpV.begin(), tmpV.end());
            }
            else{
                for(int i = 0; i<=tmpV.size()-2; i++){
                    int val=tmpV[i]+tmpV[i+1];
                    myvector.push_back(val);
                }
                    myvector.push_back(1);
            }        
        }        
        return myvector;
    }
};


int main(){  
  Solution sol;    
  vector<int> v=sol.getRow(4);

  for(int i =0; i<=v.size()-1; i++){
    cout<<v[i]<<" ";
  }
  cout<<endl;
}










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
      int compareVersion(string version1, string version2) {
        
        do {
          string v1_front, v2_front;
          int v1_fint, v2_fint, v1_found, v2_found;
          int v1_check=version1.find('.'), v2_check=version2.find('.');

          if (v1_check !=-1) v1_found=version1.find('.');
          else v1_found=version1.length();
          if (v2_check !=-1) v2_found=version2.find('.');
          else v2_found=version2.length();

          v1_front=version1.substr(0,v1_found);
          v2_front=version2.substr(0,v2_found);  
          
          cout<<v1_front<<"_hi_"<<v2_front<<endl;
          
          v1_fint=atoi(v1_front.c_str());
          v2_fint=atoi(v2_front.c_str());
          
          if (v1_fint > v2_fint) return 1;
          else if (v1_fint < v2_fint) return -1;
          else if ((v1_fint == v2_fint) && v1_check==-1 && v2_check==-1 )return 0;

          version1.erase(0,v1_found+1);
          version2.erase(0,v2_found+1);
          cout<<version1<<"_"<<version2<<endl;

        }while(!version1.empty() && !version2.empty());

        cout<<version1<<"_out_"<<version2<<endl;
        if (version1.empty() && atoi(version2.c_str())==0) return 0;
        else if (version1.empty() && atoi(version2.c_str())!=0) return -1;
        else if (version2.empty() && atoi(version1.c_str())==0) return 0;
        else if (version2.empty() && atoi(version1.c_str())!=0) return 1;

        else return 10;



        // string v1_front, v1_back, v2_front, v2_back;
        // v1_front=version1.substr(0,version1.find('.'));
        // if (version1.find('.')!=-1) v1_back=version1.substr(version1.find('.')+1);
        // else v1_back="0";
        // v2_front=version2.substr(0,version2.find('.'));
        // if (version2.find('.')!=-1) v2_back=version2.substr(version2.find('.')+1);
        // else v2_back="0";

        // int v1_fint=atoi (v1_front.c_str()), v1_bint=atoi (v1_back.c_str()), v2_fint=atoi (v2_front.c_str()), v2_bint=atoi (v2_back.c_str());
        // cout<<v1_fint<<" "<<v1_bint<<" "<<v2_fint<<" "<<v2_bint<<endl;
        // if (v1_fint > v2_fint) return 1;
        // else if (v1_fint < v2_fint) return -1;
        // else {

        //   if (v1_bint > v2_bint) return 1;
        //   else if (v1_bint < v2_bint) return -1;
        //   else return 0;
        // }
    }
};


int main(){
  Solution sol;
    string v1="19.8.3.17.5.01.0.0.4.0.0.0.0.0.0.0.0.0.0.0.0.0.00.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.000000.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.000000";
    string v2="19.8.3.17.5.01.0.0.4.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0000.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.000000";
  cout <<sol.compareVersion(v1, v2)<<endl;
}










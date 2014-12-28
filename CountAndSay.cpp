/*
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

Tag: string
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

using namespace std;

class Solution {
private:
    string StringModify(string S){
        string newstring;
        int countRepeat=1;
        for (string::iterator it = S.begin(); it !=S.end(); it++){
            // it the next is the same as the currtent *it, then loop it
            while (*(it+1) == *it){
                countRepeat++;
                it++;
            }            
            newstring+=to_string(countRepeat);
            newstring.push_back(*it);            
            countRepeat=1;
        }
        return newstring;
    }

public:
    string countAndSay(int n) {        
        string s_tmp= "1";
        while (--n > 0){
            s_tmp=StringModify(s_tmp);
        }
        return s_tmp;
    }
};



int main(){
    int n =2;
    Solution S;
    
    cout<<S.countAndSay(n)<<endl;    
    
    

}






/*
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Clarification:
- What constitutes a word?
  A sequence of non-space characters constitutes a word.
- Could the input string contain leading or trailing spaces?
  Yes. However, your reversed string should not contain leading or trailing spaces.
- How about multiple spaces between two words?
  Reduce them to a single space in the reversed string.

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
public:
    void reverseWords(string &s) {
        int str_length = s.length();        
        string rev_string="";        
        int first_time=0;
        
        // looping reversely 
        for (int i = str_length-1; i>=0; --i){
        	// once character is not a space
        	if ( s[i]!=' ' && i >=0 ){
        		string tmp;
        		// keep looping reversely 
        		while ( s[i]!=' ' && i >=0 ){
					tmp+=s[i];
        			--i;
        		}

        		// if it is the first word, then no need to add space "I am peter"  --> "peter am I", otherwise " peter am I"
        		if (first_time==0){first_time=1;}
        		else{tmp+=" ";}

        		// so now it is "retep", and reverse it to "peter" and append to the final rev_string				
				reverse(tmp.begin(), tmp.end());
				rev_string+= tmp;
        	}
        }
        if (rev_string.empty()){s="";}
        else {s=rev_string;}
    }
};



int main(){
	string S=" I am peter";
	Solution mysol;
	cout<<S<<endl;
	mysol.reverseWords(S);
	cout<<S<<endl;


}

















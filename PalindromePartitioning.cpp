/*
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
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
#include <math.h>
#include <stack>

using namespace std;

class Solution {
private:
	bool isPalindrome(string s) {
      string concise_str="";
      int idx=0;      
      while (s[idx]){
        if( isalpha(s[idx]) | isdigit(s[idx]) ) concise_str+=s[idx];        
        idx++;
      }
      int half=concise_str.length()/2;
      int leng=concise_str.length();
      for (int i=0; i<half; i++){      
        if (tolower(concise_str[i]) != tolower(concise_str[leng-1-i])) return false;        
      }
      
      
      return true;
    }

public:
    vector<vector<string> > partition(string s) {
    	vector<vector<string> > result;
    	vector<string> output;
    	DFS(s,0,output,result);
    	return result;
    }


    void DFS(string &s, int start, vector<string> &output, vector<vector<string> > &result){

    	if(start==s.size()){
    		result.push_back(output);
    		return;
    	}

    	for (int i=start; i<s.size(); i++){
    		
    		if(isPalindrome(s.substr(start,i-start+1))){
    			output.push_back(s.substr(start,i-start+1)  );    			
    			DFS(s, i+1, output, result);    			
    			output.pop_back();    			
    		}    		
    	}
    }

    void printVV(vector<vector<string> > VV){
	    for (int i=0; i<VV.size(); i++){
			for (int j=0; j<VV[i].size(); j++){
				cout<<VV[i][j]<<" ";
			}
			cout<<"----";
		}	
		cout<<endl;
    }

    void printV(vector<string> V){
	    for (int i=0; i<V.size(); i++){
			cout<<V[i]<<" ";
			
		}	
		cout<<endl;
    }



};



int main(){
	Solution sol;
	vector<vector<string> > myresult=sol.partition("aaba");
	sol.printVV(myresult);
}

















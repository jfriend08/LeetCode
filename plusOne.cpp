/*
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

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

using namespace std;


class Solution {
public:
  vector<int> plusOne(vector<int> &digits) {
    int carry=1;
    for(int i=digits.size()-1; i>=0; i--){
      cout<<"carry:" <<carry<<endl;
      int tmp=(digits[i]+carry)%10;
      carry=(digits[i]+carry)/10;  
      digits[i]=tmp;   
    }

    if (carry==1) {
      digits.insert (digits.begin(),1);
    }
    return digits;
  }
};

int main(){  
  vector<int> input, output;
  input.push_back(9);
  input.push_back(9);
  input.push_back(9);
  
  
  
  for (int i=0; i<input.size(); i++){
    cout<<input[i]<<" ";
  }
  cout<<endl;

  Solution sol;
  output=sol.plusOne(input);

  for (int i=0; i<output.size(); i++){
    cout<<output[i]<<" ";
  }
  cout<<endl;
   
  
}




/*
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

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
#include <stack> 

using namespace std;

class MinStack {
private:
  stack<int>mystack;
  stack<int>mystack_copy;
  stack<int>min;
  
  int findnextmin(){
    int mymin=2147483647;
    mystack_copy=mystack;
    while (!mystack_copy.empty()){
      int tmp=mystack_copy.top();      
      if(tmp<mymin) {        
        mymin=tmp;
      }
      mystack_copy.pop();
    }
    return mymin;          
  }

public:
    void push(int x) {
        mystack.push(x);
        if (min.empty()) min.push(x);        
        else if (x < min.top()){min.pop();min.push(x);}
    }

    void pop() {        
      if (mystack.top()==min.top()){
        mystack.pop();  
        min.pop();
        min.push(findnextmin());
      }
      else mystack.pop();        
    }

    int top() {
        return mystack.top();
    }

    int getMin() {
        return min.top();
    }
};

int main(){
  MinStack mystack;
  // push(0),push(1),push(0),getMin,pop,getMin
  mystack.push(0);  mystack.push(1);  mystack.push(0);
  
  cout<<mystack.getMin()<<endl;
  mystack.pop();
  cout<<mystack.getMin()<<endl;
  // mystack.pop();
  // cout<<mystack.getMin()<<endl;
  // mystack.pop();
  // cout<<mystack.getMin()<<endl;
}










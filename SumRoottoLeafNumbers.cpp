/*
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.

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

/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
private:
    vector<int> myQ;
    int sum=0;
public:
    
    int sumNumbers(TreeNode *root) {
        if (root==NULL) return 0;
        
        myQ.push_back(root->val);
        
        // leaf reached
        if(root->left==NULL && root->right==NULL) {
            int result=calsum();
            myQ.pop_back();
            return result;
        }
        
        sum=sumNumbers(root->left)+sumNumbers(root->right);
        
        myQ.pop_back();
        return sum;
        
    }
    
    int calsum(){
        int local_sum=0;
        for(int i=0; i<myQ.size();i++){
            local_sum+=myQ[i]*pow(10, myQ.size()-i-1);
        }
        return local_sum;
    }
};




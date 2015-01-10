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
public:
    vector<int> inorderTraversal(TreeNode *root) {
    	vector <int> inordervector;
    	if (root){
    		if (root->left){
    			inordervector= inorderTraversal(root->left);
    		}
    		
    		inordervector.push_back(root->val);

    		if (root->right){
    			vector<int> tmp=inorderTraversal(root->right);	
    			inordervector.insert(inordervector.end(),tmp.begin(),tmp.end());
    		}
    		return inordervector;
    	}
    }

    vector<int> inorderTraversal_stack(TreeNode *root) {
    	vector <int> inordervector;
    	stack<TreeNode*> mystack;
    	
    	if (root){
    		mystack.push(root);    		
    		
    		while (!mystack.empty()){    			
    			// now here, rool is always point to the top elm of the stack
    			if (root->left){
    				mystack.push(root->left);
    				root = root->left;
    			}
    			else if (root->right){
    				inordervector.push_back(mystack.top()->val);
    				mystack.pop();
    				mystack.push(root->right);
    				root = root->right;
    			}
    			
    			else{
    				inordervector.push_back(root->val);
    				mystack.pop();
    				if (!mystack.empty()){
    					root=mystack.top();
    					root->left=NULL;	
    				}
    				
    				
    			}
    		}
    		return inordervector;    		
    	}
    }

};


int main(){
  string 
  Solution sol;    

}










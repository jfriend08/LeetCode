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
    // recursive method
    bool isSymmetricRecursive(TreeNode *leftNode, TreeNode *rightNode){
        if (leftNode ==NULL && rightNode ==NULL) return true;
        else if (leftNode && rightNode && leftNode->val == rightNode->val)  {
            return ( isSymmetricRecursive(leftNode->left, rightNode->right) && isSymmetricRecursive(leftNode->right, rightNode->left) );
        }
        else if (leftNode ==NULL || rightNode ==NULL) return false;
        return false;
    }
    
    bool isSymmetric(TreeNode *root) {
        return (!root || isSymmetricRecursive(root->left, root->right) ) ;
    }

    // iterative method
    bool isSymmetric(TreeNode *root) {
        if(root){
            queue<TreeNode*> lQ, rQ;
            
            lQ.push(root->left); 
            rQ.push(root->right);
            
            while (!lQ.empty() && !rQ.empty() ){
                TreeNode* l= lQ.front();
                lQ.pop();
                TreeNode* r= rQ.front();
                rQ.pop();
                
                if(l == NULL && r == NULL) 
                    continue;
                if(l == NULL || r == NULL) 
                    return false;
                if (l->val != r->val) 
                    return false;
                
                lQ.push(l->left);
                lQ.push(l->right);
                
                rQ.push(r->right);
                rQ.push(r->left);
            }
        }
        
        return true;
        
    }
};


int main(){
  string 
  Solution sol;    

}










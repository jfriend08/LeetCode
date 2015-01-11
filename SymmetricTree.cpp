/*
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following is not:
    1
   / \
  2   2
   \   \
   3    3

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










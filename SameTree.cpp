/*
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

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

    // iterative method: 3ms
    bool isSameTree(TreeNode *p, TreeNode *q) {
        queue<TreeNode*> tree1, tree2;
        if (p && q){
            if (p->val != q->val) return false;
            tree1.push(p); tree2.push(q); 
            while (!tree1.empty() && !tree2.empty() ){
                TreeNode* ptr1= tree1.front();
                tree1.pop();
                TreeNode* ptr2= tree2.front();
                tree2.pop();
                if (ptr1== NULL && ptr2==NULL)
                    continue;
                else if (ptr1==NULL || ptr2==NULL)
                    return false;
                else if (ptr1->val == ptr2->val){
                    // need to take care for this part!!
                        tree1.push(ptr1->left);    
                        tree2.push(ptr2->left);
                        tree1.push(ptr1->right);    
                        tree2.push(ptr2->right);
                }
                else return false;
            }
            
            if (!tree1.empty() || !tree1.empty()) return false;
            else return true;
            
        }
        else if (!p && !q) return true;
        else return false;
    }    

    // recursive way: 6ms
    bool isSameTree(TreeNode *p, TreeNode *q) {
        if (p && q)
            return p->val==q->val ? isSameTree(p->left, q->left)&&isSameTree(p->right, q->right):false;
        else if (!p && !q)
            return true;
        else
            return false;
    }
};


int main(){
  string 
  Solution sol;    

}










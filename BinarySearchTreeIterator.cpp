/*
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

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
class BSTIterator {
private:
    stack <TreeNode*> myNodes;
    void LeftTransverse(TreeNode *p){
        while(p!=NULL){
            myNodes.push(p);
            p=p->left;
        }
    }

public:
    BSTIterator(TreeNode *root) {
        if(root!=NULL){
            TreeNode* ptr=root;
            LeftTransverse(ptr);
        }
    }

    /** @return whether we have a next smallest number */
    bool hasNext() {
        return myNodes.size()>0;
    }

    /** @return the next smallest number */
    int next() {
        TreeNode *firstone=myNodes.top();
        myNodes.pop();
        TreeNode *ptr=firstone->right;
        LeftTransverse(ptr);
        return firstone->val;
    }
};

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = BSTIterator(root);
 * while (i.hasNext()) cout << i.next();
 */
/*
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5

All root-to-leaf paths are:
["1->2->5", "1->3"]

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
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
  vector <string> resultVector;
public:
  void helper(TreeNode* root, string path) {
    if(!root->left && !root->right) {
      path=path+to_string(root->val);
      resultVector.push_back(path);
    } else if (!root->right && root->left) {
      path=path+to_string(root->val)+"->";
      helper(root->left, path);
    } else if (root->right && !root->left) {
      path=path+to_string(root->val)+"->";
      helper(root->right, path);
    } else {
      path=path+to_string(root->val)+"->";
      helper(root->left, path);
      helper(root->right, path);
    }
  }

  vector<string> binaryTreePaths(TreeNode* root) {
    if(root) {
      string path;
      helper(root, path);
    }
    return resultVector;
  }
};

int main() {

}
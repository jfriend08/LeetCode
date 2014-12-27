/*
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, 
level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
Tag: Tree, Breadth-first-search
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
    vector<vector<int> > levelOrderBottom(TreeNode *root) {
        
        vector<vector<int> > myallnodes; 
        
        
        if (root){
            queue <TreeNode *> myQ;
            myQ.push(root);
            
            // so myQ will saved my current working nodes
            while(!myQ.empty() ){
                
                // n will know the number of my current working nodes
                int n = myQ.size();
                
                // myvisit will save the val of my current working nodes
                vector <int> myvisit;
                
                while (n-- > 0){
                    // ptr is accessing the front of currend working nodes
                    TreeNode *ptr = myQ.front();
                    myvisit.push_back(ptr->val);
                    
                    // save ptr's left and right nodes into myQ
                    if(ptr->left){ myQ.push(ptr->left);}
                    if(ptr->right){myQ.push(ptr->right);}    
                    
                    myQ.pop();
                }
                // I can do insert, but may relocate the space everytime when I call it. not good effenciency
                myallnodes.push_back(myvisit);
            }
        }
        std::reverse(myallnodes.begin(), myallnodes.end()); 
        return myallnodes;
    }
};
/*
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the 
two subtrees of every node never differ by more than 1.

Tag: Tree, Depth-first-search

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
private:
    
    // counting the depth of the node being specified
    int countDepth ( TreeNode *TN){  
        if (!TN) {return 0;}
        else{
            int leftDepth= TN->left ? 1+countDepth(TN->left) : 1;
            int rightDepth= TN->right ? 1+countDepth(TN->right) : 1;
            return (leftDepth>rightDepth ? leftDepth : rightDepth);
        }
    }
    
public:
    bool isBalanced(TreeNode *root) {
        // the case that root not existed
        if (!root){return true;}
        
        // the case that there is no left and right subtree
        else if (!root->left && !root->right){return true;}
        
        // the case that left and right subtree existed
        else if(root->left && root->right){
            int leftDepth= countDepth(root->left);
            int rightDepth= countDepth(root->right);
            
            if (abs(leftDepth-rightDepth)>1){return false;}
            else{return (isBalanced (root->left) && isBalanced(root->right)); }//check every node in the left/right subtrees
        }
        
        // the case that either left or right subtree existed
        else{
            int leftDepth= countDepth(root->left);
            int rightDepth= countDepth(root->right);
            return (leftDepth <= 1 && rightDepth <= 1) ? true : false ;
        }

    }
};
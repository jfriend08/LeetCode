/*
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

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
// private:
//     int countShortestPath(TreeNode *TN){
//         if(!TN){return 0;}
//         else{
//             int left_shorest_path= (TN->left) ? 1+countShortestPath(TN->left) : 0;
//             int right_shorest_path= (TN->right) ? 1+countShortestPath(TN->right) : 0;
//             return ( (left_shorest_path > right_shorest_path) ? right_shorest_path : left_shorest_path );
//         }
//     }
public:
    int minDepth(TreeNode *root) {
        if (!root){return 0;}
        
        // no left and right sub nodes is the leaf
        else if (!root->left && !root->right){return 1;}
        
        // the node with both left and right sub nodes
        else if (root->left && root->right){
            int left_minDepth= minDepth(root->left);
            int right_minDepth=minDepth(root->right);
            return ( (left_minDepth>right_minDepth) ? right_minDepth+1 : left_minDepth+1 );
        }
        
        // the node with either left or right sub nodes
        else{
            if (root->left){return (minDepth(root->left) + 1);}
            else {return (minDepth(root->right) + 1 );}
        }
    }
};
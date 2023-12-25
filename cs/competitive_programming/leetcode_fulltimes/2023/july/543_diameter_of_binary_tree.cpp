#include <iostream>

/**
 * Definition for a binary tree node.*/
 struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };

class Solution {

public:

    int res=0;

    int helper(TreeNode* root) {
        
        if(root==nullptr) {
            return 0;
        }

        int l = this->helper(root->left);
        int r = this->helper(root->right);

        res = std::max(res, l+r);

        return 1+std::max(l,r);
    }

    int diameterOfBinaryTree(TreeNode* root) {

        helper(root);
        return res;
    }

};

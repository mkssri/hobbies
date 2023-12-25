#include <iostream>

// TREE Example
/*
            x
        x       x
    x
x

*/

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


class Solution{

public:
    
    // tip: murali while practising wrote return type of below function as bool instead of int
    // so few tc failed, later he figured out the following issue. here his logic is correct but weird mistake.
    int helper(TreeNode* root) {

        if(root==nullptr) return 0;

        int l = this->helper(root->left);
        int r = this->helper(root->right);

        if( (l==-1) || (r==-1) || std::abs(l-r)>1) return -1;
        return 1+std::max(l,r);

    }

    bool isBalanced(TreeNode* root) {

        if(this->helper(root)==-1)
            return false;
        return true;
    }
};

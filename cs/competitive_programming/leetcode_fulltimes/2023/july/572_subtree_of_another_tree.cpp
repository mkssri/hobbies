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
    
    // helper method, to find out if the two trees are same or not
    bool helper(TreeNode* t1, TreeNode* t2) {

        if(t1==nullptr && t2==nullptr) return true;
        if(t1==nullptr || t2==nullptr) return false;
        return (t1->val==t2->val) && helper(t1->left, t2->left) && helper(t1->right, t2->right);
    }

    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
       
        // Do BFS on root and call helper when we are on each element

        int l=0;
        TreeNode* ptr = { nullptr };
        std::deque<TreeNode*> deq = { root };

        while(deq.size()>0) {

            l = deq.size();
            for(int i=0; i<l; i++) {

                ptr = deq.front();
                deq.pop_front();

                if(this->helper(ptr, subRoot))
                    return true;
                if(ptr!=nullptr){
                    if(ptr->left) deq.push_back(ptr->left);
                    if(ptr->right) deq.push_back(ptr->right);
                }
            }
        }
        return false;
    }
};

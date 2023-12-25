class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        helper(root);
        return root;
    }

    void helper(TreeNode* node){
        if(node==NULL) {
            return;
        }

        helper(node->left);
        helper(node->right);

        TreeNode *tmp = node->left;
        node->left = node->right;
        node->right = tmp;
    }
};
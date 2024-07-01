/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */

class Solution {

    void invertBT(TreeNode* root) {
        if (!root) {
            return;
        } else {
            TreeNode* temp = root->right;
            root->right = root->left;
            root->left = temp;
        }

        invertBT(root->right);
        invertBT(root->left);
    }

public:
    TreeNode* invertTree(TreeNode* root) {

        // cout << root->right << endl;

        if (!root) {
            return root;
        }

        invertBT(root);

        return root;
    }
};
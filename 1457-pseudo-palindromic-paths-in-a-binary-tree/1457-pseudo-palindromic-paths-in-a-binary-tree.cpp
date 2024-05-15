/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
 #include<iostream>    
#include<vector> 
#include<algorithm>
class Solution {




public:


     int countPseudoPalindromicPaths(TreeNode* node, vector<int>& digitCount) {
        if(!node) {
            return 0;
        }

        digitCount[node->val]++;

        if(!node->left && !node->right) {
            int oddCount = 0;
            for(int count : digitCount) {
            if(count % 2 != 0) oddCount++;
        }


    if(oddCount <= 1) {
        digitCount[node->val]--;
        return 1;
    } else {
        digitCount[node->val]--;
        return 0;
    }
        }

    int leftPaths = countPseudoPalindromicPaths(node->left, digitCount);
    int rightPaths = countPseudoPalindromicPaths(node->right, digitCount);

        digitCount[node->val]--;
        
        return leftPaths + rightPaths;
     }
    int pseudoPalindromicPaths (TreeNode* root) {
        vector<int> digitCount(10,0);
        return countPseudoPalindromicPaths(root, digitCount);
    }
};
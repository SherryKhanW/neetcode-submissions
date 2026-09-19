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

class Solution {
public:
    // This should check if the two trees are EXACTLY the same (structure + values)
    bool isMatch(TreeNode* ptr1, TreeNode* ptr2) {
        if (ptr1 == nullptr && ptr2 == nullptr) return true;
        if (ptr1 == nullptr || ptr2 == nullptr) return false;

        if (ptr1->val != ptr2->val) return false;

        return isMatch(ptr1->left, ptr2->left) && isMatch(ptr1->right, ptr2->right);
    }

    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if (subRoot == nullptr) return true;   // empty subRoot is always a subtree
        if (root == nullptr) return false;     // no place left to match

        // if they match starting at this node
        if (isMatch(root, subRoot)) return true;

        // otherwise search left or right
        return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
    }
};

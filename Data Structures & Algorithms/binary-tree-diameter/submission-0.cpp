class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        int best = 0;
        height(root, best);
        return best;
    }

private:
    int height(TreeNode* node, int& best) {
        if (!node) return -1;
        int l = height(node->left, best);
        int r = height(node->right, best);
        best = max(best, l + r + 2);
        return 1 + max(l, r);
    }
};
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function isSubtree(root: TreeNode | null, subRoot: TreeNode | null): boolean {
    // we've reached the end of the tree without finding a match, so its false
    if (!root) {
        return false;
    }

    // an empty tree is considered a subtree of any tree, so we return true.
    if (!subRoot) {
        return true;
    }

    if (isSameTree(root, subRoot)) {
        return true;
    }

    // checks if either of the left/right of the main tree contains the subtree
    return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
};

function isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {
    if (!p && !q) {
        return true;
    }

    if (p && q && p.val === q.val) {
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }

    return false;
}

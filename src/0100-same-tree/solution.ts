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

function isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {
    if (!p && !q) {
        // both null, this means we are on the same nodes, this is good!
        return true;
    }

    if (p && q && p.val === q.val) {
        // iterate until we hit base case
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right)
    }

    return false;
};

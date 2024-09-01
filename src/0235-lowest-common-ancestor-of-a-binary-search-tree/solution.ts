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

function lowestCommonAncestor(root: TreeNode | null, p: TreeNode | null, q: TreeNode | null): TreeNode | null {
	/**
    * There are 3 scenarios:
    * 1. we go right -> cuz p and q are bigger than what we currently are at
    * 2. we go left -> cuz p and q are smaller than what we currently are at
    * 3. we are at the answer
    *        -> p < current and q > current, means we found the LCA, split decision scenario
    *        -> p = current and q < current, means we found the LCA
    * Time: O(log n) cuz we only ever iterate through half the tree at a time.
    */
    if (!root) {
        // should never occur
        return null;
    } else if (root.val < p.val && root.val < q.val) {
        root = lowestCommonAncestor(root.right, p, q);
    } else if (root.val > p.val && root.val > q.val) {
        root = lowestCommonAncestor(root.left, p, q);
    }
    return root;

};

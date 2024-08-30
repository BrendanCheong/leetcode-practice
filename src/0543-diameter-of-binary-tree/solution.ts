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

function diameterOfBinaryTree(root: TreeNode | null): number {
    /**
     * The diameter of the binary tree is defined as the length of the longest path 
     * between any two nodes in the tree. This path may or may not pass through the root.
     * 
     * To calculate the diameter, we need to explore every node and compute the longest 
     * path that can be formed by using that node as the highest point in the path (i.e., 
     * considering both its left and right subtrees).
     * 
     * The diameter is then the maximum of these values.
     */
    let diameter = 0;

    function maxDepth(node: TreeNode | null): number {
        if (!node) {
            return 0;
        }

        // Go through the longest left depth and right depth
        const leftDepth = maxDepth(node.left);
        const rightDepth = maxDepth(node.right);

        // Update the diameter if the path through this node is larger than the current max diameter
        diameter = Math.max(diameter, leftDepth + rightDepth);

        // Return the maximum depth of this node's subtree
        return 1 + Math.max(leftDepth, rightDepth);
    }

    maxDepth(root);
    return diameter;
}

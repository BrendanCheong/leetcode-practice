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

function goodNodes(root: TreeNode | null): number {
    /**
    * This solution is all about keeping track of the previously visited max value
    * while we DFS and go through the left and right trees of the bst.
    * As we move through the tree, we can validate if good node based on the ancestor's most maximum value
    
    */
    let count = 0;

    function dfs(node: TreeNode | null, prevMax: number): void {
        if (!node) {
            return;
        }

        if (node.val >= prevMax) {
            count++;
            // update the prevMax in that path
        }
        prevMax = Math.max(prevMax, node.val);
        dfs(node.left, prevMax);
        dfs(node.right, prevMax);
    }
    dfs(root, root.val);
    return count;
};

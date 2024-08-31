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

 class TreeHeight {
    isBalanced: boolean;
    height: number;

    constructor(isBalanced: boolean, height: number) {
        this.isBalanced = isBalanced;
        this.height = height;
    }
 }

function isBalanced(root: TreeNode | null): boolean {
   function dfs(root: TreeNode): TreeHeight {
        if (!root) {
            // null node is balanced
            // by default a single node is a balanced tree of height 1
            return new TreeHeight(true, 0);
        }

        // balanced is difference in height is not more than 1
        // but must also check previous heights
        const leftTree = dfs(root.left);
        const rightTree = dfs(root.right);
        const isBalanced = leftTree.isBalanced && 
            rightTree.isBalanced && 
            Math.abs(leftTree.height - rightTree.height) <= 1;
        
        // iterator, we need to return the result of the calculated height and if calculated balance
        return new TreeHeight(isBalanced, 1 + Math.max(leftTree.height, rightTree.height));
   }

   return dfs(root).isBalanced;
};

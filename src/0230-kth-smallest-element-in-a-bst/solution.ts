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

function kthSmallest(root: TreeNode | null, k: number): number {
    /**
    * Not sure if theres a O(1) space solution. But the O(n) way would be to just sort using
    * in-order traversal: which is left -> middle -> right
    */
    const result = new Array<number>();
    function inOrderTraversal(node: TreeNode | null): void {
        if (!node) {
            return;
        }
        inOrderTraversal(node.left);
        result.push(node.val);
        inOrderTraversal(node.right);
    }
    inOrderTraversal(root);
    console.log(result);
    return result[k - 1];

};

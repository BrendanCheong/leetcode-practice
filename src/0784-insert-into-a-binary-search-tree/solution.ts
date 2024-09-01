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

function insertIntoBST(root: TreeNode | null, val: number): TreeNode | null {
    // if > than current val insert at right
    // if < than current val insert at left
    // if at the end null, just insert
    if (!root) {
        return new TreeNode(val);
    }
    else if (root.val < val) {
        root.right = insertIntoBST(root.right, val);
    }
    else {
        root.left = insertIntoBST(root.left, val);
    }

    return root;
};

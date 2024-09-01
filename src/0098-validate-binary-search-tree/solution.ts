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

function isValidBST(root: TreeNode | null): boolean {
    /**
    When you go left from a node:
    You’re moving to a smaller number.
    So, you need to remember that the value can’t be bigger than the node you just left. This node sets the upper limit.
    
    When you go right from a node:
    You’re moving to a bigger number.
    Now, the value can’t be smaller than the node you just left. This node sets the lower limit.
     */
    function isValid(root: TreeNode | null, lowerBound: number, upperBound: number): boolean {
        if (!root) {
            return true;
        }
        // Check if root.val is within the bounds, current root cant be outside lower or upper bounds
        if (
            (lowerBound !== null && root.val <= lowerBound) || 
            (upperBound !== null && root.val >= upperBound)
        ) {
            return false;
        }
        // We move to left, smaller number is met, move the upperbound to keep window in-tact
        return isValid(root.left, lowerBound, root.val) &&
            // We move to right, bigger number is met, so we should move the lowerbound up as well to keep window in-tact
            isValid(root.right, root.val, upperBound);
    }

    return isValid(root, null, null);
};

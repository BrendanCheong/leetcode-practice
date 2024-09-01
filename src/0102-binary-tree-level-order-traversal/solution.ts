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

function levelOrder(root: TreeNode | null): number[][] {
    const q = new Queue.Queue();
    const result = new Array();
    q.enqueue(root);

    if (!root) {
        return [];
    }

    while (!q.isEmpty()) {
        const val = new Array();
        const queueSize = q.size();
        // this is layer by layer level
        for (let i = 0; i < queueSize; i++) {
            // Go through entire queue, node level
            const curr = q.dequeue();
            val.push(curr.val)
            if (curr.left) {
                q.enqueue(curr.left)
            }
            if (curr.right) {
                q.enqueue(curr.right);
            }
        }
        result.push(val);
    }
    return result;
};

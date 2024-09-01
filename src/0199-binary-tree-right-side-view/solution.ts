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

function rightSideView(root: TreeNode | null): number[] {
    /***
     * Basically the right side view node, is the node at the last item to be processed in the queue
     * of the BFS algo
     */
    const q = new Queue.Queue();
    const result = [];
    if (!root) {
        return result;
    }

    q.enqueue(root);
    while (!q.isEmpty()) {
        const lengthOfQueue = q.size();
        for (let i = 0; i < lengthOfQueue; i++) {
            const curr = q.dequeue();
            // If we are the last item to be processed, means most rightmost node
            if (i === lengthOfQueue - 1) {
                result.push(curr.val)
            }
            if (curr.left) {
                q.enqueue(curr.left);
            }

            if (curr.right) {
                q.enqueue(curr.right);
            }
        }
    }

    return result;
};

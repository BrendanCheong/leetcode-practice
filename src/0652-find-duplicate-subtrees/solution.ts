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

function findDuplicateSubtrees(root: TreeNode | null): Array<TreeNode | null> {
    /**
     * We need to do post-order traversal: left -> right -> middle, we need to go through
     * the left tree and the right tree and compare them to check for duplicate trees
     * then we need to serialise the tree (basically store it into a hashmap) and count the number
     * of times the tree appears, as trees that appear more than once is the answer
     * Time: O(N * N) traverse the tree and count the number of subtrees.
     * Space: O(N * N) store entire tree and subtress
     */
    const visited = new Map<string, number>();
    const result = [];
    function postOrder(node: TreeNode | null) {
        if (!node) {
            return '$';
        }
        const leftTree = postOrder(node.left);
        const rightTree = postOrder(node.right);

        // serialise tree
        const serializedTree = `${node.val},${leftTree},${rightTree}`;
        
        // check if we saw the tree already
        if (!visited.has(serializedTree)) {
            visited.set(serializedTree, 1);
        }
        else {
            // if we saw the tree already, only add to result once
            if (visited.get(serializedTree) === 1) {
                result.push(node);
            }
            // update count of tree
            visited.set(serializedTree, visited.get(serializedTree) + 1);
        }

        return serializedTree;
    }
    postOrder(root);
    return result;
};

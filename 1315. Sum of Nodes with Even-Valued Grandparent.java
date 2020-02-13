/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public int sumEvenGrandparent(TreeNode root) {
        return helper(root, 1, 1);
    }

    public int helper(TreeNode node, int p, int gp) {
        if (node == null) return 0;
        return helper(node.left, node.val, p) + helper(node.right, node.val, p) + (gp % 2 == 0 ? node.val : 0);
    }
    // java不能给函数参数赋默认值，不像C++
    // public int sumEvenGrandparent(TreeNode root, int parent = 1, int gp = 1) {
    //     return root ? sumEvenGrandparent(root.left, root.val, parent) + sumEvenGrandparent(root.right, root.val, parent) + (gp % 2 == 0 ? root.val : 0) : 0;
    // }
}
// 以下代码不对，因为只考虑了level，而没有考虑当前level的节点的祖父节点是不是偶数
//     private int res;
//     private Set<Integer> mySet;
//     public int sumEvenGrandparent(TreeNode root) {
//         res = 0;
//         mySet = new HashSet();
        
//         helper(root, 0);
        
//         return res;
//     }

//     private void helper( TreeNode node, int level ) {
//         level++;
//         if( node != null ){
//             if( mySet.contains(level) ) res += node.val;
//             if( node.val % 2 == 0) mySet.add( level + 2 );
//             helper(node.left, level);
//             helper( node.right, level);
//         }
//     }
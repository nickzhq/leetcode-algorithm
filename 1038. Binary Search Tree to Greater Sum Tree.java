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
//     public TreeNode bstToGst(TreeNode root) {
//         helper(root, 0);
//         return root;
//     }
    
//     private int helper(TreeNode root, int maxNum) {
//         if(root.right != null) maxNum = helper(root.right, maxNum);
//         root.val += maxNum;
//         maxNum = root.val;
//         if(root.left != null) maxNum = helper(root.left, maxNum);
        
//         return maxNum;
//     }
    int sumNum = 0;
    public TreeNode bstToGst(TreeNode root) {
        if(root == null) return null;
        bstToGst(root.right);
        root.val += sumNum;
        sumNum = root.val;
        bstToGst(root.left);
        return root;
    }
}
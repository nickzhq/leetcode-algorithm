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
    public TreeNode bstFromPreorder(int[] preorder) {
        if (preorder.length <= 0) { return null;}
        TreeNode root = new TreeNode(preorder[0]);
        for(int idx = 1; idx < preorder.length; ++idx) {
            buildTree(root, preorder[idx]);
        }
        return root;
    }
    private void buildTree(TreeNode root, int val) {
        if( root.val > val ) {
            if(root.left == null) { root.left = new TreeNode(val); }
            else { buildTree(root.left, val); }
        }else{
            if(root.right == null) { root.right = new TreeNode(val); }
            else{ buildTree(root.right, val); }
        }
    }
}
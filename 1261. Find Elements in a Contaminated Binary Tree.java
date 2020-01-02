/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class FindElements {
    // List<Integer> myList = new LinkedList<>();
    Set<Integer> mySet = new HashSet<>();
    public FindElements(TreeNode root) {
        dfs(root, 0);
    }
    
    private void dfs(TreeNode root, int val) {
        if(root == null) return;
        root.val = val;
        mySet.add(val);
        dfs(root.left, 2 * val + 1);
        dfs(root.right, 2 * val + 2);
    }
    
    public boolean find(int target) {
        return mySet.contains(target);
    }
}
// class FindElements {
//     // List<Integer> myList = new LinkedList<>();
//     Set<Integer> myList = new HashSet<>();
//     public FindElements(TreeNode root) {
        
//         root.val = 0;
//         Queue<TreeNode> q = new LinkedList<>();
//         q.add( root );
        
//         while( !q.isEmpty() ) {
//             TreeNode cur = q.remove();
//             myList.add(cur.val);
            
//             if(cur.left != null) {
//                 cur.left.val = 2 * cur.val + 1;
//                 q.add(cur.left);
//             }
//             if(cur.right != null) {
//                 cur.right.val = 2 * cur.val + 2;
//                 q.add(cur.right);
//             }
//         }
//     }
    
//     public boolean find(int target) {
//         return myList.contains(target);
//     }
// }

/**
 * Your FindElements object will be instantiated and called as such:
 * FindElements obj = new FindElements(root);
 * boolean param_1 = obj.find(target);
 */
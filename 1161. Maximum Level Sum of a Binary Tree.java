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
    public int maxLevelSum(TreeNode root) {
        List<Integer> levels = new ArrayList<Integer>();
        traverse(root, levels, 0);

        return levels.indexOf( Collections.max(levels) ) + 1;
    }
    
    public void traverse(TreeNode r, List<Integer> l, int level){
        if(r != null){
            if(l.size() - 1 >= level){
                int t = l.get(level) + r.val;
                l.set(level, t);
            }else{
                l.add(r.val);
            }
            
            traverse(r.left, l, level + 1);
            traverse(r.right, l, level + 1);
        }
    }
}

// class Solution {
//     public int maxLevelSum(TreeNode root) {
//         Queue<TreeNode> myQ = new LinkedList<>();
        
//         myQ.add(root);
        
//         int maxL = 1;
//         int maxSum = root.val;
//         int level = 1;
        
//         while( !myQ.isEmpty() ) {
//             int sum = 0;
//             int size = myQ.size();
            
//             for( int i = 0; i < size; ++i ) {
//                 TreeNode node = myQ.poll();
//                 sum += node.val;
                
//                 if( node.left != null ) myQ.add(node.left);
//                 if( node.right != null ) myQ.add(node.right);
//             }
            
//             if( sum > maxSum ) {
//                 maxSum = sum;
//                 maxL = level;
//             }
            
//             level += 1;
//         }
        
//         return maxL;
//     }
// }
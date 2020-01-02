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
    Map<Integer, List<TreeNode>> memo = new HashMap();
    public List<TreeNode> allPossibleFBT(int N) {
        if( !memo.containsKey(N) ) {
            List<TreeNode> res = new LinkedList();
            if ( N == 1 ) {
                res.add( new TreeNode(0) );
            } else if (N % 2 == 1) {
                for( int i = 0; i < N; i++ ) 
                    for( TreeNode ltree: allPossibleFBT(i) )
                        for( TreeNode rtree: allPossibleFBT( N - i -1) ) {
                            TreeNode node = new TreeNode(0);
                            node.left = ltree;
                            node.right = rtree;
                            res.add(node);
                        }
            }
            memo.put(N, res);
        }
        return memo.get(N);
    }
}
// class Solution {
//     public List<TreeNode> allPossibleFBT(int N) {
//         List<TreeNode> res = new LinkedList<>();
//         if(N == 1) res.add( new TreeNode(0) );
        
//         for ( int i = 1; i < N; i += 2) {
//             for( TreeNode ltree: allPossibleFBT(i) )
//                 for( TreeNode rtree: allPossibleFBT( N - i - 1) ) {
//                     TreeNode node = new TreeNode(0);
//                     node.left = ltree;
//                     node.right = rtree;
//                     res.add(node);
//                 }
//         }
//         return res;
//     }
// }
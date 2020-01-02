class Solution {
    List<List<Integer>> res;
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        res = new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        path.add(0);
        dfs(graph, 0, path);
        return res;
    }
    private void dfs(int[][] graph, int index, List<Integer> path) {
        if( index == graph.length - 1) {
            res.add(new ArrayList<>(path));
        } else {
            for( int node: graph[index] ) {
                path.add( node );
                dfs(graph, node, path);
                path.remove( path.size() - 1 ); // path.remove(index)
            }
        }
    }
}
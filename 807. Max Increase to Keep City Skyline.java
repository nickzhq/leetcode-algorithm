class Solution {
    public int maxIncreaseKeepingSkyline(int[][] grid) {
        int[] ver = new int[grid[0].length];
        int[] hor = new int[grid.length];
        int res = 0;
        
        for(int i = 0; i < grid.length; ++i) {
            for(int j = 0; j < grid[i].length; ++j) {
                hor[i] = Math.max(hor[i], grid[i][j]);
                ver[j] = Math.max(ver[j], grid[i][j]);
            }
        }
        
        for(int i = 0; i < grid.length; ++i) {
            for(int j = 0; j < grid.length; ++j) {
                res += Math.min(hor[i],ver[j]) - grid[i][j];
            }
        }
        
        return res;
    }
}
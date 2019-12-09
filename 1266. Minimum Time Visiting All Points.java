class Solution {
    public int minTimeToVisitAllPoints(int[][] points) {
        if( points.length < 2 ) { return 0; }
        int totalMove = 0;
        for( int idx = 0; idx < points.length - 1; ++idx) {
            int x = Math.abs( points[idx+1][0] - points[idx][0] );
            int y = Math.abs( points[idx+1][1] - points[idx][1] );
            totalMove += Math.max(x,y);
        }
        return totalMove;
    }
}
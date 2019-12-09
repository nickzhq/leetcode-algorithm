class Solution {
    public int[][] flipAndInvertImage(int[][] A) {
        int len = A[0].length;
        for(int[] row: A) {
            for( int idx = 0; idx < (len+1) / 2; ++idx) {
                int temp = row[idx] ^ 1;
                row[idx] = row[len - 1 - idx] ^ 1;
                row[len - 1 - idx] = temp;
            }
        }
        return A;
    }
}
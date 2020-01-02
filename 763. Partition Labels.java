class Solution {
    public List<Integer> partitionLabels(String S) {
        int[] lastChar = new int[26];
        for(int idx = 0; idx < S.length(); ++idx) {
            lastChar[S.charAt(idx) - 'a'] = idx;
        }
        
        int left = 0, right = 0;
        List<Integer> res = new ArrayList<Integer>();
        for( int idx = 0; idx < S.length(); ++idx ) {
            right = Math.max( right, lastChar[S.charAt(idx) - 'a'] );
            if (idx == right) {
                res.add(idx - left + 1);
                left = idx + 1;
            }
        }
        
        return res;
    }
}
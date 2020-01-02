class Solution {
    HashSet<Integer> visited = new HashSet<>();
    HashSet<String> res = new HashSet<>();
    public int numTilePossibilities(String tiles) {
        backtrace(tiles, "");
        return res.size();
    }
    public void backtrace(String tiles, String cur) {
        if( !cur.equals("") && !res.contains(cur) ) {
            res.add(cur);
        }
        for(int idx = 0; idx < tiles.length(); ++idx) {
            if( !visited.contains(idx) ) {
                visited.add(idx);
                backtrace(tiles, cur + tiles.charAt(idx));
                visited.remove(idx);
            }
        }
    }
}
class Solution {
    public List<List<Integer>> groupThePeople(int[] groupSizes) {
        int n = groupSizes.length;
        List<List<Integer>> res = new ArrayList<>();
        HashMap<Integer, List<Integer>> hm = new HashMap<>();
        
        for(int i = 0; i < n; ++i) {
            int cur = groupSizes[i];
            List<Integer> temp = new ArrayList<>();
            if( hm.containsKey(cur) ) temp = hm.get(cur);
            
            temp.add(i);
            hm.put(cur, temp);
            
            if(temp.size() == cur) {
                res.add(temp);
                hm.remove(cur);
            }
        }
        
        return res;
    }
}
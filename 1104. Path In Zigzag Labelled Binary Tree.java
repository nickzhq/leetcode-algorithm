class Solution {
    public List<Integer> pathInZigZagTree(int label) {
        LinkedList<Integer> res = new LinkedList<>();
        res.add(label);
        // x > 0时，Math.floor(x) 相当于 Math.round(x-0.5)
        int level = (int)(Math.round( Math.log(label) / Math.log(2) - 0.5 ) + 1);
        int curVal = label;
        while( level > 1 ) {
            // int parent = (Math.pow(2, level-1) + Math.pow(2, level) - 1 - curVal) / 2;
            int parent = ( (1 << (level-1)) + (1 << level) - 1 - curVal ) / 2;
            res.addFirst(parent);
            
            curVal = parent;
            level--;
        }
        
        return res;
    }
}
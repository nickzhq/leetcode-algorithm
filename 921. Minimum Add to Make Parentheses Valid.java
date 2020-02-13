class Solution {
    public int minAddToMakeValid(String S) {
        int ans = 0, bal = 0;
        for (int i = 0; i < S.length(); ++i) {
            bal += S.charAt(i) == '(' ? 1 : -1;
            // It is guaranteed bal >= -1
            if (bal == -1) {
                ans++;
                bal++;
            }
        }

        return ans + bal;
    }
}
// class Solution {
//     public int minAddToMakeValid(String S) {
//         Stack<Character> res = new Stack();
        
//         for( int i = 0; i < S.length(); ++i) {
//             if( !res.empty() && res.peek() == '(' && S.charAt(i) == ')' )  res.pop();
//             else res.push(S.charAt(i));
//         }
        
//         return res.size();
//     }
// }
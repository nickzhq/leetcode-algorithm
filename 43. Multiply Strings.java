class Solution {
    public String multiply(String num1, String num2) {
        int num1length = num1.length();
        int num2length = num2.length();
        char[] res = new char[ num1length + num2length ];
        int carry = 0;
        
        // calculate the product of each digital
        for( int i = num1length - 1; i >= 0; --i ) {
            for( int j = num2length - 1; j >= 0; --j ) {
                res[i + j +1] += (num1.charAt(i) - '0') * (num2.charAt(j) - '0'); // 记录每个位置的值，由于是char类型，会被显示成ASCII
            }
        }
        // calculate the carry
        for( int i = res.length - 1; i >= 0; --i ) {
            res[i] += carry; // 把进位加进当前数值
            carry = res[i] / 10; // 目的是因为记录进位
            res[i] %= 10; // 记录最末位数字
            res[i] += '0'; // 加个字符0，这样可将结果转成字符数字，例如 '0'+'2' = 2(ASCII中的2)         
        }
        
        // 计算有几个0在前面
        int begin = 0;
        while( begin < res.length - 1 && res[begin] == '0' ) 
            begin++;
        
        return new String( res, begin, res.length - begin );
    }
}
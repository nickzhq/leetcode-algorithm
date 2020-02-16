/*
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?
*/
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        unsigned int res = 2;// binary: 00000000 00000000 00000000 00000010
    	int record = 0;
    	for (int i = 0; i < 32; i++) {
    		if ((n | 1) == n) record = 1;
    		else record = 0;
    		n = n >> 1;
    		res |= record;
    		if (i == 31) break;
    		res = res << 1;
    	}
        return res;
    }
};

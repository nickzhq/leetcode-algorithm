class Solution {
public:
    int lengthOfLastWord(string s) {
        //using the I/O streams without any boost
        istringstream buf(s);
        istream_iterator<string> beg(buf); // string iterator
        istream_iterator<string> end;  // end-of-stream iterator
        
        vector<string> word(beg, end);
        if( word.empty() ) return 0;
        return word[word.size() - 1].size();
    }
};

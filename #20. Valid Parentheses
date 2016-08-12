class Solution {
public:
    bool isValid(string s) {
        stack<char> myStack;
        for( auto t: s) {
            if( t == '(' || t == '{' || t == '[') myStack.push(t);
            else if( t == ')' || t == '}' || t == ']' ) {
                if( myStack.empty() || myStack.top() - t > 2) return false;
                myStack.pop();
            }
        }
        return myStack.empty();
    }
};

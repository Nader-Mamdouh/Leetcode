class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<long long> st;
        for (const string& token : tokens) {
            if (token == "+") {
                long long x = st.top();
                st.pop();
                long long y = st.top();
                st.pop();
                st.push(x + y);
            } else if (token == "-") {
                long long x = st.top();
                st.pop();
                long long y = st.top();
                st.pop();
                st.push(y - x); 
            } else if (token == "*") {
                long long x = st.top();
                st.pop();
                long long y = st.top();
                st.pop();
                st.push(x * y);
            } else if (token == "/") {
                long long x = st.top();
                st.pop();
                long long y = st.top();
                st.pop();
                if (x != 0) 
                    st.push(y / x); 
                else
                    return 0; 
            } else {
                st.push(stoll(token));
            }
        }
        return st.top();
    }
};

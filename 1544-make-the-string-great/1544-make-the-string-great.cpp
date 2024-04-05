class Solution {
public:
    string makeGood(string s)
    {
        stack<char> st;

        for (int i = 0; i < s.size(); i++) {
            if (!st.empty() && ((islower(st.top()) && isupper(s[i]) && tolower(st.top()) == tolower(s[i])) ||
                (isupper(st.top()) && islower(s[i]) && tolower(st.top()) == tolower(s[i])))) {
                st.pop();
            }
            else {
                st.push(s[i]);
            }
        }

        string result = "";
        while (!st.empty()) {
            result = st.top() + result;
            st.pop();
        }
        return result;
        
    }
};
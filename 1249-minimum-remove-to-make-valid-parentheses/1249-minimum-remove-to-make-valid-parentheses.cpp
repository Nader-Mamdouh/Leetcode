class Solution {
public:
    string minRemoveToMakeValid(string s) 
    {
        stack<int> st;
        string ans = "";
        for (int i = 0; i < s.size(); i++) 
        {
            if (s[i] >= 'a' && s[i] <= 'z')
            {
                ans += s[i];
            }
            else if (s[i] == '(')
            {
                st.push(ans.size());  
                ans += s[i];
            }
            else if (s[i] == ')')
            {
                if (!st.empty())
                {
                    ans += s[i];
                    st.pop();
                }
            }
        }
        
        while (!st.empty())
        {
            ans.erase(st.top(), 1);  
            st.pop();
        }

        return ans;   
    }
};
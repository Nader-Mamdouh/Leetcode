class Solution {
public:
    bool checkValidString(string s) 
    {
        stack<char> st;
        int ans = 0;
        for (int i = 0; i < s.size(); i++) 
        {
            
            if (s[i] == '(')
            {
                if (st.empty())
                {
                    st.push(s[i]);
                }
                else{
                    if(st.top()==')')
                    {
                        return false;
                    }
                    else{
                        st.push(s[i]);
                    }
                }
                
                
            }
            else if (s[i] == '*')
            {
                ans += 1;
            }
            else
            {
                if (st.empty())
                {
                    st.push(s[i]);
                }
                else if (st.top() == '(' and s[i] == ')')
                {
                    
                    st.pop();
                }
            }
        }
        if (ans >= st.size() || st.empty())
        {
            return true;
        }
        else {
            return false;
        }   
    }
};
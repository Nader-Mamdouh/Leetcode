class Solution {
public:
    string removeStars(string s)
    {
        int n=s.size();
        stack<int>st;
        for (int i=0;i<n;i++)
        {
            if (s[i]=='*')
            {
                st.pop();
            }
            else
            {
                st.push(s[i]);
            }
            
        }
        int k=st.size();
        string h="";
        while(k--)
        {
            h+=st.top();
            st.pop();
        }
        reverse(h.begin(),h.end());
        return h;
    }
};
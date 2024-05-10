class Solution {
public:
    int scoreOfString(string s) {
        int n=s.size();
        int sum=0;
        for (int i=1;i<n;i++)
        {
            sum+=abs((s[i]-'a')-(s[i-1]-'a'));
        }
        return sum;
    }
};
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& num1, vector<int>& num2) 
    {
        vector<int> ans;
        int n = num1.size();
        int h = num2.size();
        
        for (int i = 0; i < n; i++)
        {
            bool found = false;
            for (int j = 0; j < h; j++)
            {
                if (num1[i] == num2[j])
                {
                    int greater = -1;
                    for (int k = j + 1; k < h; k++)
                    {
                        if (num2[k] > num1[i])
                        {
                            greater = num2[k];
                            break;
                        }
                    }
                    ans.push_back(greater);
                    found = true;
                    break;
                }
            }
            if (!found)
            {
                ans.push_back(-1);
            }
        }
        
        return ans;
    }
};

#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& num1, vector<int>& num2) 
    {
        vector<int> ans;
        unordered_map<int, int> nextGreater;
        int n = num1.size();
        int h = num2.size();
        for (int i = 0; i < h; i++)
        {
            int greater = -1;
            for (int j = i + 1; j < h; j++)
            {
                if (num2[j] > num2[i])
                {
                    greater = num2[j];
                    break;
                }
            }
            nextGreater[num2[i]] = greater;
        }
        for (int i = 0; i < n; i++)
        {
            ans.push_back(nextGreater[num1[i]]);
        }

        return ans;
    }
};

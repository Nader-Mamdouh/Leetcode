class Solution {
public:
    int maxSubArray(vector<int>& nums) 
    {
        long long ans = LLONG_MIN; // Initialize ans with the minimum possible value
        long long prefix_sum = 0;
        long long min_prefix_sum = 0;

        for (int i = 0; i < nums.size(); i++) {
            prefix_sum += nums[i];
            ans = max(ans, prefix_sum - min_prefix_sum);
            min_prefix_sum = min(min_prefix_sum, prefix_sum);
        }

        return ans;   
    }
};
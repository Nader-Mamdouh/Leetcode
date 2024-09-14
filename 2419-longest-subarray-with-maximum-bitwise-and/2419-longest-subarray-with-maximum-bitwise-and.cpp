class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int n=nums.size();
        int ans=0,l=0;
        int m=*max_element(nums.begin(),nums.end());
        for(int i=0;i<n;i++){
            if(nums[i]==m)l++;
            else l=0;
            ans=max(ans,l);
        }
        return ans;
    }
};
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        int n = nums.size();
        unordered_map<int, int> mp;

        vector<int> ans;
        for(int i = 0; i < n; i++) {
            int comp = target - nums[i];

            if(mp.find(comp) != mp.end()) {
                ans.push_back(i);
                ans.push_back(mp[comp]);
                break;
            }
            mp[nums[i]] = i;
        }

        return ans;

    }
};
class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int zeroLocation = -1;
        int left = 0;
        int maxLength = 0;
        bool zeroEncountered = false;

        for(int right = 0; right < nums.size(); right++) {
            if(nums[right] == 0) {
                if(zeroEncountered) {
                    maxLength = max(maxLength, right - left - 1);
                    left = zeroLocation + 1;
            } else {
                zeroEncountered = true;
                    }
                    zeroLocation = right;
                }
        }

        if(!zeroEncountered) {
            maxLength = std::max(maxLength, static_cast<int>(nums.size()) - 1);
        } else {
        maxLength = std::max(maxLength, static_cast<int>(nums.size()) - left - (zeroEncountered ? 1 : 0));
        }
        return maxLength;
    }
};
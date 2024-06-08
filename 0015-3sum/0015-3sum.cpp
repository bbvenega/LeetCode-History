class Solution {
public:
    bool isZero(int i, int j, int k) {
        return (i + j + k == 0);
    }

    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;
        int size = nums.size();

        // Step 1: Sort the array
        sort(nums.begin(), nums.end());

        // Step 2: Iterate through the array
        for(int i = 0; i < size - 2; i++) {
            // Step 3: Skip duplicate values for the first number
            if(i > 0 && nums[i] == nums[i - 1]) continue;

            int j = i + 1;      // The next number after i
            int k = size - 1;   // The last number in the array

            while(j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                if(sum == 0) {
                    // Found a valid triplet
                    ans.push_back({nums[i], nums[j], nums[k]});

                    // Step 4: Skip duplicate values for the second number
                    while(j < k && nums[j] == nums[j + 1]) j++;
                    // Step 5: Skip duplicate values for the third number
                    while(j < k && nums[k] == nums[k - 1]) k--;

                    j++;
                    k--;
                } else if(sum < 0) {
                    j++;
                } else {
                    k--;
                }
            }
        }

        return ans;
    }
};

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int size = nums.size();


        if(nums.empty()) {
            return 0;
        } else if(size == 1) {
            return 1;
        } else {
        int counter = 1;
        int currCounter= 1;
        for(int i = 0; i < size - 1;i++) {
            // cout << "Comparing " << nums[i+1] << " to " << nums[i] + 1 << endl;
            if(nums[i+1] == nums[i] + 1) {
                currCounter++;
            } else if ( nums[i+1] == nums[i]) {
                continue;
            }
            else {
                // cout << counter + 1;
                currCounter = 1;
            }
            counter = max(currCounter, counter);
        }

        return counter;
    }
    }
};
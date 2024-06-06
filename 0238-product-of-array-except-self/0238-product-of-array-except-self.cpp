class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        
        vector<int> ans;
        int product = 1;
        int zeroCounter = 0;
        for(int i = 0; i < nums.size(); i++) {
            
            if(nums[i] != 0) {
                 product = product * nums[i];  
            }   else {
                zeroCounter++;
            }
    }

    // cout << "PRoduct is: " << product << endl;
        for(int i = 0; i < nums.size(); i++) {

            if(zeroCounter > 1) {
                ans.push_back(0);
            }
            if(zeroCounter <= 0) {
                ans.push_back(product / nums[i]);
            } if(zeroCounter == 1) {
                    if(nums[i] == 0) {
                // cout << "Pushing: " << product << endl;
            ans.push_back(product);
            } else {
                ans.push_back(0);
                }
            }
        }

        return ans;
    }
};
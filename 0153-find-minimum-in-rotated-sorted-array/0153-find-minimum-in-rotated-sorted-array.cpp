class Solution {
public:
    int findMin(vector<int>& nums) {
        int temp1;
        int least = nums[0];
        
    
         for(auto entry : nums) {
            if (entry < least) {
                least = entry;
            }
         }

         while(nums[0] != least) {
            int temp = nums[0];
            for(int i = 0; i < nums.size(); i++) {
                
                int shift = i + 1;

                if(i >= nums.size() - 1) {
                    nums[i] = temp;
                    break;
                }
                nums[i] = nums[shift];
                
            }
            }

                     for(auto entry : nums) {
            cout << entry;
         }
        cout << endl;
         return least;
         }


    
};
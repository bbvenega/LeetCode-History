class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<int> sol(2,0);
        int i = 0;
        while(i < nums.size()) {
            if(nums[i] == nums[i+ 1]) {
                if(nums[i] == i+1) {
                    sol[0] = nums[i];
                    i +=1;
                    while(i < nums.size() && nums[i] == i) {
                    i +=1;
                }
                sol[1] = i;
                break;
                } else {
                sol[0] = nums[i];
                while(i > -1 && nums[i] != i + 1) {
                    i -= 1;
                }

                if(i < 0) {
                    sol[1] = 1;
                } else {
                    sol[1] = i +2;
                }
                    break;
            }
            }
        i+= 1;


    }
            return sol;
    }
};
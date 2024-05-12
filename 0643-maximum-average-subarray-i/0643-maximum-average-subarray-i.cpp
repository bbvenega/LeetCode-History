class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        
        double greatest = -99999999999999;
        double sum = 0;

    for(int j = 0; j < k; j++) {
        sum += nums[j];
    }

    double average = sum /k;
    greatest = max(greatest, average);
        for(int i = k; i < nums.size(); i++) {
            sum += nums[i] - nums[i-k];
            average = sum / k;
            greatest = max(greatest, average);
            


        }

        return greatest;
    }
};
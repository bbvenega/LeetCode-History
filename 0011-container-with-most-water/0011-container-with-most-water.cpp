class Solution {
public:
    int maxArea(vector<int>& height) {
        

        int greatest = 0;
        int left = 0;
        int right = height.size() - 1;

        while(left < right) {

            int currentHeight = min(height[left], height[right]); 
            int currentWidth = right - left;
            int currentArea = currentWidth * currentHeight;

            greatest = max(currentArea, greatest);


            if(height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return greatest;
    }
};
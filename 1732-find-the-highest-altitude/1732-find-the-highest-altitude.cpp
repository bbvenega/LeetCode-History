class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        
        int greatest = 0;
        int curAlt = 0;
        int ans;

        for(int i = 0; i < gain.size(); i++) {
            curAlt += gain[i];
            if(curAlt > greatest) {
                greatest = curAlt;
                // ans = gain[i];
            }
        }
    return greatest;
    }
};
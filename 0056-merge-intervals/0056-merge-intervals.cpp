class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {

        if(intervals.size() == 1) {
            return intervals;
        }
       vector<vector<int>> ans;
       

        sort(intervals.begin(), intervals.end(), [](const auto& a, const auto& b) {
            return a[0] < b[0];
        }); 
       for(int i = 0; i < intervals.size() - 1; i++) {

        if(intervals[i][1] >= intervals[i+1][0]) {
            intervals[i+1][0] = min(intervals[i+1][0], intervals[i][0]);
            intervals[i+1][1] = max(intervals[i+1][1], intervals[i][1]);
        } else {
            ans.push_back(intervals[i]);
        }
       } 

        ans.push_back(intervals[intervals.size()-1]);
       for(int i = 0; i < ans.size(); i++) {
        printf("[%d,%d] ", ans[i][0],ans[i][1]);
       }

       cout << endl;

       return ans;
    }
};
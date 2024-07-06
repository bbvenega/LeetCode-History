class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {

        vector<vector<int>> ans;
        vector<int> combo;
        sort(candidates.begin(), candidates.end());
        backTrack(ans, combo, candidates, target, 0);
        return ans;
    }

    void backTrack(vector<vector<int>>& ans, vector<int>& combo,
                   vector<int>& candidates, int remain, int start) {
        if (remain < 0) {
            return;
        } else if (remain == 0) {
            ans.push_back(combo);
        }

        else {
            for (int i = start; i < candidates.size(); i++) {
                combo.push_back(candidates[i]);
                backTrack(ans, combo, candidates, remain - candidates[i], i);
                combo.pop_back();
            }
        }
    }
};
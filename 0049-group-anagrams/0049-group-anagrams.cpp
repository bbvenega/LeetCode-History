class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;

        for(auto entry : strs) {
            string word = entry;
            sort(word.begin(), word.end());
            mp[word].push_back(entry);
        }

        vector<vector<string>> ans;

        for(auto entry : mp) {
            ans.push_back(entry.second);
        }

        return ans;
    }
};
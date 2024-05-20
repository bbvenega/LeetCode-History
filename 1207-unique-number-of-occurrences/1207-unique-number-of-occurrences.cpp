class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {

        map<int, int> mp;

        for(auto entry: arr) {
            mp[entry]++;
        }
         
         unordered_set<int>s;
        for(auto entry : mp) {
            s.insert(entry.second);
            }

    return mp.size() == s.size();
    }
};
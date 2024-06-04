class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
       unordered_map<int, int> mp;
       priority_queue<pair<int,int>>pq;

       for(auto entry : nums) {
    mp[entry]++;
       } 
           for(auto entry : mp) {
    pq.push({entry.second, entry.first});
       } 

      vector<int> ans;

      while(k-- && !pq.empty()) {
        ans.push_back(pq.top().second);
        pq.pop();
      }


       return ans;
    }
};
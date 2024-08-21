class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char, int> freq;

        for (char ch : s) {
            freq[ch]++;
        }

        priority_queue<pair<int, char>> pq;
        for (auto val : freq) {
            pq.push(make_pair(val.second, val.first));
        }

        string ans = "";

        while (!pq.empty()) {

            for (int i = 0; i < pq.top().first; i++) {
                ans += pq.top().second;
            }
            pq.pop();
        }

        return ans;
    }
};
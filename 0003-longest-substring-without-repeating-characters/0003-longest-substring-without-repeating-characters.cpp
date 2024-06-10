class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.empty()) return 0;
        if (s.size() == 1) return 1;

        string subs;
        int len = 0;
        int i = 0;
        int j = 0;

        while (j < s.size()) { 
            auto it = find(subs.begin(), subs.end(), s[j]);
            if (it == subs.end()) {
                // No duplicate found, add s[j] to subs
                subs += s[j];
                j++;
            } else {
                // Duplicate found, update len and move i forward
                len = max(static_cast<int>(subs.size()), len);
                subs.erase(0, subs.find(s[j]) + 1);
                i++;
            }
        }
        // Update len one last time in case the longest substring was found at the end
        len = max(static_cast<int>(subs.size()), len);

        return len;
    }
};

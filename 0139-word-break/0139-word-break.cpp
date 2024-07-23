class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {

        unordered_set<string> words;

        for (int i = 0; i < wordDict.size(); i++) {
            words.insert(wordDict[i]);
        }

        int n = s.size();
        vector<bool> dp(n + 1);
        dp[0] = true;

        for (int i = 0; i <= n; i++) {
            for (int j = i - 1; j >= 0; j--) {
                if (dp[j]) {
                    
                    string subs = s.substr(j, i - j);

                    if (words.find(subs) != words.end()) {
                        cout << subs << endl; 
                        dp[i] = true;
                    }
                }
            }
        }

        return dp[n];
    }
};
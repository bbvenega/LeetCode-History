class Solution {
public:
    string removeStars(string s) {
        

        stack<char> word;

 
        for(char ch : s) {
            if(ch == '*') {
                word.pop();
            } else {
                word.push(ch);
            }
        }

        string ans;
        while(!word.empty()) {
            ans += word.top();
            word.pop();
        }

        reverse(ans.begin(), ans.end());
        return ans;
    }
};
class Solution {
public:
    vector<string> generateParenthesis(int n) {

        vector<string> ans;
        string res = "(";
        int end = n * 2;
        backtrack(n, 1, 0, end, ans, res);
        return ans;
    }

    void backtrack(int n, int open, int close, int end, vector<string>& ans,
                   string res) {
        // printf("backtrack: res: %s open: %d close: %d\n", res.c_str(), open,
        //        close);
        if (res.size() == end && open == n && close == n) {
            // printf("**PUSHING BACK: %s **  open: %d close: %d\n",
            //        res.c_str(), open, close);
            ans.push_back(res);
            return;
        }

        if (open < n) {

            // printf("** res: %s ** is not currently valid ADDING ) open: %d "
            //        "close: %d\n",
            //        res.c_str(), open + 1, close);
            backtrack(n, open + 1, close, end, ans, res + "(");
        }
        if (close < n && open > close) {

            // printf("** res: %s ** is not currently valid ADDING ( open: %d "
            //        "close: %d\n",
            //        res.c_str(), open, close + 1);
            backtrack(n, open, close + 1, end, ans, res + ")");
        }
    }
};
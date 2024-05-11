class Solution {
public:
    bool isSubsequence(string s, string t) {

        bool checker = true;
        int foundIndex = 0;
        string str;

        if(s.empty()) {
            return true;

        }

        if(t.empty()) {
            return false;
        }

        for(int i = 0; i < s.length(); i++) {

                for(int j = foundIndex; j < t.length(); j++) {
                   if(s[i] == t[j]) {
                    foundIndex = j + 1;
                    i++;
                    str += t[j];
                   } 
}
            }

        

        cout << str << endl;
        if(str == s) {
            checker = true;
        } else {
            checker = false;
        }
        return checker;
    }
};
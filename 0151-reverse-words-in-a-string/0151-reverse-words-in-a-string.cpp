

class Solution {
public:
    string reverseWords(string s) {
        

        vector<string> words;
        string token;
        string ans;

        stringstream ss(s);
        while(getline(ss, token, ' ')) {
            cout << token << endl;
            if(!token.empty()) {
                 cout << "Added: " << token << endl;
words.push_back(token);
            } 
            
        }

        for(int i = words.size() - 1; i >=0 ; i--) {
            if(i != 0) {
            ans = ans  + words[i] + " ";
        } else {
            ans = ans + words[i];
        }
        }


return ans;
    }
};
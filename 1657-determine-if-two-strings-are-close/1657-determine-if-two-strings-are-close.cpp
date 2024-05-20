class Solution {
public:
    bool closeStrings(string word1, string word2) {
        
        if(word1.size() != word2.size()) {
            return false;
        }

        map<char, int> mp1;
        map<char, int> mp2;

        for(auto it : word1) {
            mp1[it]++;
        }
        for(auto it : word2) {
            mp2[it]++;
        }

    string word1Freq;
    string word2Freq;
    string word1FreqChar;
    string word2FreqChar;

        for(auto entry : mp1) {
            word1FreqChar += entry.first;
            word1Freq += to_string(entry.second);
        }
        for(auto entry : mp2) {
            word2FreqChar += entry.first;
            word2Freq += to_string(entry.second);
        }


        if(word1FreqChar != word2FreqChar) {
            return false;
        }

        sort(word1Freq.begin(), word1Freq.end());
        sort(word2Freq.begin(), word2Freq.end());
                
        if(word1Freq != word2Freq) {
            return false;
        }

        return true;
    }
};
class Solution {
public:
    int longestPalindrome(vector<string>& words) {
        unordered_map<string, int> freq;
        int palindromeLength = 0;
        bool centerUsed = false;

        // Count frequency of each word
        for (string word : words) {
            freq[word]++;
        }

        for (auto& [word, count] : freq) {
            string reversedWord = string({word[1], word[0]});
            
            // Handle symmetric words like "aa", "bb"
            if (word == reversedWord) {
                palindromeLength += (count / 2) * 4;
                if (count % 2 == 1) {
                    centerUsed = true; // Reserve one for the center if possible
                }
            } 
            // Handle pairs like "ab" and "ba"
            else if (freq.find(reversedWord) != freq.end()) {
                int minCount = min(count, freq[reversedWord]);
                palindromeLength += minCount * 4;
                freq[reversedWord] = 0; // Set to 0 to avoid recounting
            }
        }

        // Add center part if there's an odd count symmetric word
        if (centerUsed) {
            palindromeLength += 2;
        }

        return palindromeLength;
    }
};

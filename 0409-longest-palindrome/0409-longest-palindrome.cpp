class Solution {
public:

    int longestPalindrome(string s) {
        int oddCount = 0;
        unordered_map<char, int> ump;
        for(char ch : s) {
            ump[ch]++;
            if (ump[ch] % 2 == 1)
                oddCount++;
            else    
                oddCount--;
        }
        if (oddCount > 1)
            return s.length() - oddCount + 1;
        return s.length();
    }
};


// unordered_map<char, int> freq;
// for (char ch : s) {
//     freq[ch]++;
// }

// int total = 0;
// bool center = false;

// if (freq.size() == 1) {
//     return s.size();
// }
// for (auto entry : freq) {
//     if (entry.second % 2 == 0) {
//         total += entry.second;
//     }
//     if (entry.second == 1 && center == false) {
//         total += 1;
//         center = true;
//     }
// }

// return total;
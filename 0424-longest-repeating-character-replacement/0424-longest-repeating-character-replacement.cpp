class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> alphabets; // Map to keep track of character counts
        int ans = 0; // Store the maximum length of the substring found
        int left = 0; // Left pointer for the sliding window
        int right = 0; // Right pointer for the sliding window
        int maxf = 0; // Maximum frequency of any character in the current window

        for (right = 0; right < s.size(); right++) {
            // Increment the count of the current character
            alphabets[s[right]] = 1 + alphabets[s[right]];
            
            // Update the max frequency of any character in the window
            maxf = max(maxf, alphabets[s[right]]);
            
            // If the current window size minus the most frequent character count is greater than `k`
            if ((right - left + 1) - maxf > k) {
                // Reduce the count of the character at the left pointer and shrink the window
                alphabets[s[left]] -= 1;
                left++;
            } else {
                // Update the maximum length found
                ans = max(ans, (right - left + 1));
            }
        }

        return ans; // Return the maximum length of the valid substring found
    }
};

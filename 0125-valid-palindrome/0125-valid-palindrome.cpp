class Solution {
public:
    bool isPalindrome(string s) {
        int i = 0;
        int j = s.size() - 1;

        while (i < j) {
            // Skip non-alphanumeric characters
            while (i < j && !isalnum(s[i])) i++;
            while (i < j && !isalnum(s[j])) j--;

            // Convert characters to lowercase
            char a = tolower(s[i]);
            char b = tolower(s[j]);

            // Compare characters
            if (a != b) {
                return false;
            }

            i++;
            j--;
        }

        return true;
    }
};

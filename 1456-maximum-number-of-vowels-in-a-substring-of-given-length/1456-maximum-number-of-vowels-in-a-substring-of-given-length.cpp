#include <string>

class Solution {
public:

    int countVowels(string s) {
        int counter = 0;
        string vowels = "aeiou";
        for(int i = 0; i < s.length(); i++) {
            if(vowels.find(s[i]) != string::npos) {
                // cout << vowels.find(s[i]) << endl;
                counter++;
            }
        }
        return counter;
    }
    int maxVowels(string s, int k) {
        
        int stringLength = s.length();
        int maxVowelCount = 0;
        int vowelCount = 0;
        string window = s.substr(0, k);

        vowelCount = countVowels(window);
        maxVowelCount = vowelCount;

        for(int i = k; i < stringLength; i++) {
            
            if(window[0] == 'a' || window[0] == 'e' || window[0] == 'i' || window[0] == 'o' || window[0] == 'u') {
                 vowelCount--;
                //  cout << firstWindow << endl;
            } 
            window.erase(0,1);
            
            window += s[i];
            if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u') {
                vowelCount++;
                // cout << "Window: " << window << ", Vowel count: " << vowelCount << ", Max count: " << maxVowelCount << endl;
}
            maxVowelCount = max(maxVowelCount, vowelCount);

        }

        return maxVowelCount;
    }


};
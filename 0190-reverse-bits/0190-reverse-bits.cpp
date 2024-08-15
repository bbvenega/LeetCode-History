class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t reverse = 0;

        int bit = 0;
        int count = 32;
        while (count > 0) {
            bit = n & 1;

            if (bit == 0) {
                reverse = (reverse << 1) | 0;
            } else {
                reverse = (reverse << 1) | 1;
            }

            n = n >> 1;
            count--;
        }

        cout << reverse << endl;
        return reverse;
    }
};
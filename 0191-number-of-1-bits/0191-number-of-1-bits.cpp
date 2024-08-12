class Solution {
public:
    int hammingWeight(int n) {

        string binary = "";

        while (n / 2 > 0) {
            int rem = n % 2;
            binary = to_string(rem) + binary;
            n = n / 2;
        }

        if (n == 1) {
            binary = to_string(n) + binary;
        }

        int counter = 0;

        for (int i = 0; i < binary.size(); i++) {
            string num = binary.substr(i, 1);
            if (stoi(num) == 1) {
                counter++;
            }
        }

        return counter;
    }
};
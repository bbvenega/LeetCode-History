class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        vector<int> remainder(60,0);
        int counter = 0;

        for(auto val : time) {
            int rem = val % 60;
            int comp = (60 - rem) % 60;
            
            counter += remainder[comp];
            remainder[rem]++;
        }

        return counter;
    }
};
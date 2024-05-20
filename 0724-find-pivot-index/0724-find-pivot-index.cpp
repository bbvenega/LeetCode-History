class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        
        int totalLeft = 0;
        int totalRight = 0;

        for(int i = 1; i < nums.size(); i++) {
            totalRight += nums[i];
        }

        int index = -1;

            cout << "START" << endl;
                    cout << "totalLeft = " << totalLeft << endl;
            cout << "totalRight = " << totalRight << endl;

                    if(totalRight == 0 && totalLeft == 0) {
                    return 0;
                }


        for(int counter = 1; counter < nums.size(); counter++) {

            cout << counter << endl;
            totalLeft += nums[counter - 1];
            totalRight -= nums[counter];

            cout << "totalLeft = " << totalLeft << endl;
            cout << "totalRight = " << totalRight << endl;


                        if(totalLeft == totalRight) {

                index = counter;
                break;
            }
        
        }
        
        return index;
    }
};
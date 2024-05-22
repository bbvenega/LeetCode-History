class Solution {
public:
    int equalPairs(vector<vector<int>>& grid) {
        
        map<int, vector<int>> rows;
        map<int, vector<int>> columns;
    int counter = 0;
        for(int i = 0; i < grid.size(); i++) {
            for(int j = 0; j < grid[i].size(); j++) {
                columns[j].push_back(grid[i][j]);
                rows[i].push_back(grid[i][j]);
                // cout << "Adding "<< grid[i][j] << " to the " <<  i << " row " << endl;

                // cout << "Adding "<< grid[j][i] << " to the " <<  i << " column " << endl;
                        //    cout<< endl;
            }
        }



        for(int i = 0; i < grid.size(); i++) {
            for(int j = 0; j < grid.size(); j++) {
                 if (rows[i] == columns[j]) {
                counter++;
            }
            
            }
        }

        return counter;
    }
};
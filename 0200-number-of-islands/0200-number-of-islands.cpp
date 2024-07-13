class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int counter = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    counter++;
                    backTrack(grid, i, m, n, j);
                    // come back to?
                }
            }
        }

        return counter;
    }

    void backTrack(vector<vector<char>>& grid, int i, int m, int n, int j) {
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == '0') {
            return;
        }

        grid[i][j] = '0';

        backTrack(grid, i + 1, m, n, j);
        backTrack(grid, i - 1, m, n, j);
        backTrack(grid, i, m, n, j + 1);
        backTrack(grid, i, m, n, j - 1);
    }
};
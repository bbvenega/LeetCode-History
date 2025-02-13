class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]

        for r in range(0,9):
            for c in range(0,9):

                val = board[r][c]

                if val == ".":
                    continue
                
                if val in rows[r]:
                    return False
                
                if val in cols[c]:
                    return False

                gridIndex = (r // 3) * 3 + (c // 3)
                # print(f"Grid index: {gridIndex}")

                if val in grid[gridIndex]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                grid[gridIndex].add(val)
        
        return True
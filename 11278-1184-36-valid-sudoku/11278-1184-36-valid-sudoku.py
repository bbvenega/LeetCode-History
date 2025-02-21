class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = [set() for _ in range(9)]

        
        for  r in range(9):
            for c in range(9):

                val = board[r][c]

                if val == '.':
                    continue

                if val in rows[r]:
                    return False
                
                if val in cols[c]:
                    return False
                
                gridIdx = (r // 3) * 3 + (c // 3)

                if val in grids[gridIdx]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                grids[gridIdx].add(val)
        
        return True
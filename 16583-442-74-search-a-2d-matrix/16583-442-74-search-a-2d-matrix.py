class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1
        mid = 0

        # Do a binary search with the rows by checking if the midpoint row contains the target boundaries
        while low <= high:
            mid = low + ((high - low) // 2)
            # print(f"l: {low} h: {high} and m:{mid}")

            if matrix[mid][0] == target:
                return True
            
            # if the target is greater than the greatest value in the row, has to be a greater row
            if matrix[mid][-1] < target:
                low = mid + 1
            
            # if the target is less than the smallest value in the row, has to be a lesser row
            elif matrix[mid][0] > target:
                high = mid - 1
            
            # if neither condition above is met, the target is in the current row
            else: 
                break

            
        low = 0
        high = len(matrix[mid]) - 1
        
        # Just do a binary search within the row
        while low <= high:
            mid_new = low + ((high - low) // 2)

            if matrix[mid][mid_new] == target:
                return True
            
            if matrix[mid][mid_new] < target:
                low = mid_new + 1
            else:
                high = mid_new - 1
        
        return False
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        mid = 0
        while top <= bottom:    
            mid = top + ((bottom - top) // 2)
            print(f"t: {top} b: {bottom} m: {mid}")
        
            if matrix[mid][0] == target:
                return True
            
            if matrix[mid][0] > target:
                bottom = mid - 1
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                break


        left = 0
        right = len(matrix[mid]) - 1

        while left <= right:
            mid_r = left + ((right - left) // 2)

            if matrix[mid][mid_r] == target:
                return True

            if matrix[mid][mid_r] < target:
                # print(f"l = {mid + 1}")
                left = mid_r + 1
            else:
                right = mid_r - 1

            # print(f"l: {left} r: {right} mid_r: {mid_r}")
        return False
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top = 0
        bottom = len(matrix) - 1
        mid = 0
        while top <= bottom:
            mid = top + ((bottom - top ) // 2)
            # print(f"t: {top} b: {bottom} m: {mid}")


            if matrix[mid][0] == target:
                return True

            
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else: 
                break
        

        left = 0
        right = len(matrix[mid]) - 1
        while left <= right:
            mid_r = left + ((right - left) // 2)
            # print(f"l: {left} r: {right} m_r: {mid_r}")

            if matrix[mid][mid_r] == target:
                return True
            
            if target < matrix[mid][mid_r]:
                right = right - 1
            else:
                left = left + 1

        return False
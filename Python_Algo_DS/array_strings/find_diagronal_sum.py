
class Solution3:
    def diagonalSum(self, mat) -> int:
        n = len(mat)
        _sum = 0
        for row in range(n):
            _sum += mat[row][row]
            if row != n-1-row:
                _sum += mat[row][n-1-row]

        return _sum
        
        
mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]

print(Solution3().diagonalSum(mat))

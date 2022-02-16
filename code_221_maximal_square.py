import math
class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0]) # assuming all rows have the same number of columns
        if n == 1 and m == 1:
            return 1 if int(matrix[0][0]) == 1 else 0
        
        dp = [ [0]*(m+1) for _ in range(n+1) ]

        max = 0
        for row in range(1,n+1):
            for col in range(1,m+1):
                dp[row][col] = int(matrix[row-1][col-1])
                if dp[row][col] == 1:
                    left = dp[row][col-1]
                    up = dp[row-1][col]
                    diagonal = dp[row-1][col-1]
                    dp[row][col] += min(left, up, diagonal)
                    if dp[row][col] > max:
                        max = dp[row][col]
        return max*max

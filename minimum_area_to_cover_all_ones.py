class Solution(object):
    def minimumArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        x1 = y1 = float('inf')
        x2 = y2 = float('-inf')

        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 1:
                    x1 = min(x1, i)
                    y1 = min(y1, j)
                    x2 = max(x2, i)
                    y2 = max(y2, j)

        return int((x2 - x1 + 1) * (y2 - y1 + 1))
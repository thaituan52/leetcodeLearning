#https://leetcode.com/problems/game-of-life

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        def count_neighbors(r, c):
            cnt = 0
            for i in range(r-1, r+2):
                for j in range(c-1, c+2):
                    if (i == r and j == c) or i < 0 or j < 0 or i >= rows or j >= cols:
                        continue
                    if abs(board[i][j]) == 1:  # check old state
                        cnt += 1
            return cnt

        # Step 1: Mark transitions
        for r in range(rows):
            for c in range(cols):
                live_neighbors = count_neighbors(r, c)

                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = -1  # alive → dead
                if board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] = 2   # dead → alive

        # Step 2: Finalize the board
        for r in range(rows):
            for c in range(cols):
                if board[r][c] > 0:
                    board[r][c] = 1
                else:
                    board[r][c] = 0        
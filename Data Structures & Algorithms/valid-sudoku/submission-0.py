class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        length = len(board)

        rows = {}
        cols = {}
        squares = {}

        for outerIndex in range(length):
            for innerIndex in range(length):
                num = board[outerIndex][innerIndex]

                if num == ".":
                    continue

                square = (outerIndex // 3, innerIndex // 3)

                # Check for duplicates
                if num in rows.get(outerIndex, set()):
                    return False

                if num in cols.get(innerIndex, set()):
                    return False

                if num in squares.get(square, set()):
                    return False

                # Initialize sets when necessary
                if outerIndex not in rows:
                    rows[outerIndex] = set()

                if innerIndex not in cols:
                    cols[innerIndex] = set()

                if square not in squares:
                    squares[square] = set()

                # Add current number
                rows[outerIndex].add(num)
                cols[innerIndex].add(num)
                squares[square].add(num)

        return True
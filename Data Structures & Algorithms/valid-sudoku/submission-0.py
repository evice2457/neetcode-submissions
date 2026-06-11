from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check the row
        for row in board:
            if not self.checkRepeat(row):
                return False
            
        
        list_column = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                list_column[j].append(board[i][j])

        # Check the column
        for col in list_column:
            if not self.checkRepeat(col):
                return False
        
        # Check the square 
        for row_box in range(0,9,3):
            for col_box in range(0,9,3):
                square = []
                for i in range(3):
                    for j in range(3):
                        square.append(board[row_box+i][col_box+j])
                if not self.checkRepeat(square):
                    return False
        return True

        

    # Check each line 
    def checkRepeat(self, line: List[str]) -> bool:
        count = Counter(line)
        for key in count:
            if count[key] > 1 and key != ".":
                return False
        return True
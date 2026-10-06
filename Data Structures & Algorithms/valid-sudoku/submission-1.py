class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # /// TIME TO REDO IT FROM SCRATCH //////


        # # first time encountering this question, so took some help.... ahhhhh
        # # we'll come back to this one later and try it completely on our own haha (cos i know i can forget it lol)

        # rows = [set() for _ in range(9)]
        # cols = [set() for _ in range(9)]
        # boxes = [set() for _ in range(9)]

        # # so like we've created 3 sets for keeping track of numbers in rows, columns and 3x3 boxes, gotchaa???

        # for r in range(9):
        #     for c in range(9):

        #         # empty cell, nothing to check here
        #         if board[r][c] == ".":
        #             continue

        #         num = board[r][c]

        #         # now's time to figuring out which 3x3 box this particular cell belongs to..........
        #         box = (r // 3) * 3 + (c // 3)

        #         # if the number already exists in its row, column or box then we've got a duplicate -> means invalid sudoku
        #         if num in rows[r] or num in cols[c] or num in boxes[box]:
        #             return False

        #         # number is valid so far, let's store it in all 3 places
        #         rows[r].add(num)
        #         cols[c].add(num)
        #         boxes[box].add(num)

        # # made it through the whole board without finding a duplicate
        # # the valid sudoku is hereee :^*^:
        # return True











        # practice time!!!!!!!
        
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    continue
                
                num = board[r][c]
                box = (r//3)*3+(c//3)

                if num in rows[r] or num in columns[c] or num in boxes[box]:
                    return False
                
                rows[r].add(num)
                columns[c].add(num)
                boxes[box].add(num)

        return True
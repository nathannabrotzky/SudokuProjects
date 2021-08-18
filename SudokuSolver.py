POSSIBILITIES = [1,2,3,4,5,6,7,8,9]
BLOCK_SETS = [[1,2,3],[4,5,6],[7,8,9]]

board = [[0,0,0,2,6,0,7,0,1],
        [6,8,0,0,7,0,0,9,0],
        [1,9,0,0,0,4,5,0,0],
        [8,2,0,1,0,0,0,4,0],
        [0,0,4,6,0,2,9,0,0],
        [0,5,0,0,0,3,0,2,8],
        [0,0,9,3,0,0,0,7,4],
        [0,4,0,0,5,0,0,3,6],
        [7,0,3,0,1,8,0,0,0]]

def printBoard(board):
    print_output = ""
    print("=======================")
    row_index = 0
    col_index = 0
    for row in board:
        row_index += 1
        for val in row:
            col_index += 1
            print_output += "|" + str(val)
            if col_index % 3 == 0:
                print_output += "| "
        col_index = 0
        print(print_output)
        if row_index % 3 == 0:
            print("=======================")
        print_output = ""
def checkCompletion(board):
    completion = True
    for row in board:
        for val in row:
            if val == 0:
                completion = False
    return completion
def validateBoard(board):
    validation = True
    for row in POSSIBILITIES:
        for col in POSSIBILITIES:
            if board[row - 1][col - 1] in POSSIBILITIES:
                val_count = 0
                for val in board[row - 1]:
                    if val == board[row - 1][col - 1]:
                        val_count += 1
                if val_count > 1:
                    validation = False
                val_count = 0
                for r_index in POSSIBILITIES:
                    for c_index in POSSIBILITIES:
                        if col == c_index and board[r_index - 1][c_index - 1] == board[row - 1][col - 1]:
                            val_count += 1
                if val_count > 1:
                    validation = False
                val_count = 0
                for r_blocks in BLOCK_SETS:
                    for c_blocks in BLOCK_SETS:
                        if row in r_blocks and col in c_blocks:
                            for r_index in r_blocks:
                                for c_index in c_blocks:
                                    if board[r_index - 1][c_index - 1] == board[row - 1][col - 1]:
                                        val_count += 1
                if val_count > 1:
                    validation = False
    return validation
def findOptions(board, blanks, r_index, c_index):
    if board[r_index - 1][c_index - 1] == 0:
        found_numbers = []
        for val in board[r_index - 1]:
            if val != 0:
                found_numbers.append(val)
        for row in POSSIBILITIES:
            for col in POSSIBILITIES:
                if col - 1 == c_index - 1 and board[row - 1][col - 1] != 0:
                    found_numbers.append(board[row - 1][col - 1])
                    break
        for r_block in BLOCK_SETS:
            for c_block in BLOCK_SETS:
                if r_index in r_block and c_index in c_block:
                    for row in r_block:
                        for col in c_block:
                            if board[row - 1][col - 1] != 0:
                                found_numbers.append(board[row - 1][col - 1])
                    break
        found_numbers = list(dict.fromkeys(found_numbers))
        elimination = [1,2,3,4,5,6,7,8,9]
        for nums in found_numbers:
            elimination.remove(nums)
        blanks.append([[r_index,c_index],elimination])
    return blanks
def solve_standard(board):
    changes_count = 0
    blanks = []
    for r_index in POSSIBILITIES:
        for c_index in POSSIBILITIES:
            blanks = findOptions(board, blanks, r_index, c_index)
    for blank in blanks:
        if len(blank[1]) == 1:
            changes_count += 1
            board[blank[0][0] - 1][blank[0][1] - 1] = blank[1][0]
    if changes_count > 0:
        return False
    else:
        return True


printBoard(board)
print(validateBoard(board))
print()
print()
change_check = solve_standard(board)
while (not(change_check)):
    printBoard(board)
    change_check = solve_standard(board)
print(checkCompletion(board))
print(validateBoard(board))

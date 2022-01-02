#Standard solving algorithm with standard terminal output

import boards

#formatting of board
def print_board(bo):

    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            
            if j == len(bo[0]) - 1:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j #row, column

    return False

#return False if not a valid input, return True if valid
def valid(bo, num, pos):

    #Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num:
            return False
    
    #Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num:
            return False
    
    #Check box
    box_row = pos[0] // 3
    box_col = pos[1] // 3

    for row_i in range(box_row * 3, box_row * 3 + 3):
        for col_i in range(box_col * 3, box_col * 3 + 3):
            if bo[row_i][col_i] == num:
                return False
    
    return True #Pass all conditions

#backtracking and recursion 
def solve(bo):

    find = find_empty(bo)
    if not find:
        return True
    else: 
        row, col = find
    
    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0
    
    return False



# print_board(boards.board)
# solve(boards.board)
# print("------------------------")
# print_board(boards.board)



            
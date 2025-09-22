def solve_sudoku(board,count):
    row,col=find_cell_MRV(board,count)
    if row == -1:
        return True
    for num in range(1,10):
        if is_valid(board,row,col,num,count):
            board[row][col]=num
            if solve_sudoku(board,count):
                return True
        board[row][col]=0
        count[1]+=1
    return False
def find_cell_MRV(board,count):
    best_row,best_col=-1,-1
    min_candidates=10
    for row in range(0,9):
        for col in range(0,9):
            candidates=count_candidates(board,row,col,count)
            if candidates < min_candidates:
                min_candidates = candidates
                best_row,best_col=row,col
              
    return best_row,best_col

def count_candidates(board,row,col,count):
    if board[row][col]>0:
        return 11
    valid=0
    for i in range(1,10):
        if is_valid(board,row,col,i,count):
                valid+=1
    if valid>0:
        return valid 
    else: 
        return 11
       
def is_valid(board,row,col,num,count):
    for i in range(0,9):
        if board[row][i]==num:
            count[0]+=1
            return False
        if board[i][col]==num:
            count[0]+=1
            return False
    
    #checking 3x3 box 
    x=row-row%3
    y=col-col%3
    for i in range(x,x+3):
        for j in range(y,y+3):
            if board[i][j]==num:
                count[0]+=1
                return False
    return True

def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))

def main():
    board = [
        [2, 0, 0, 0, 3, 0, 0, 4, 0],
        [0, 3, 0, 6, 0, 0, 0, 0, 7],
        [0, 0, 9, 0, 0, 7, 1, 0, 8],
        [0, 0, 4, 0, 7, 2, 0, 0, 0],
        [0, 2, 5, 0, 8, 1, 9, 0, 0],
        [1, 0, 3, 0, 0, 6, 0, 0, 5],
        [0, 0, 0, 0, 2, 0, 4, 0, 0],
        [4, 0, 6, 8, 0, 0, 0, 7, 0],
        [5, 0, 0, 9, 0, 0, 3, 0, 0]
    ]
    count=[0,0]

    if solve_sudoku(board,count):
        print("Solved Sudoku:")
        print_board(board)
    else:
        print("No solution exists.")
    print("Prevented minimum wrong directions going sequentially that is from 0 to 9: ",count[0])
    print("backtracked: ",count[1])
if __name__ == "__main__":
    main()
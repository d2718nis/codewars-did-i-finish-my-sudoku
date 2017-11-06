def done_or_not(board):
    """Check if Sudoku board is valid or not.

    Keyword arguments:
    board -- Sudoku board as a list[list_lines]

    Return "Finished!" if the board is valid, otherwise return "Try again!".
    """
    for x in range(9):
        if (
            # Rows
            len(set(board[x])) < 9 or
            # Columns
            len(set(board[a][x] for a in range(9))) < 9 or
            # Regions
            len(set(board[x//3*3+a//3][x//3*3+a%3] for a in range(9))) < 9
        ):
            # Not valid
            return "Try again!"
    # Valid
    return "Finished!"
